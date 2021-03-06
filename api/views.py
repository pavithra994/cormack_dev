#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status, response, permissions
from django_mailbox.models import Mailbox
from urllib.parse import urlparse
from uuid import UUID
from api.models import FileUpload, JobNotification

from urllib.parse import quote as urlencode

import json
import re
import boto
import requests
import base64

# TODO: move to ocom
from rest_framework.views import View, APIView
from api.models import Job, Repair, XeroOAuth2Information
from api.xero_utils import createJobInvoice, createJobPurchaseOrder, createRepairInvoice, createRepairPurchaseOrder
from ocom.utils.auth_override import JSONWebTokenParamAuthentication
from ocom_xero.models import XeroEntity
from ocom_xero.serializer import XeroEntitySerializer
from ocom_xero.utils import connectToXero

#NEWCODE
from django.core.cache import caches
from xero import Xero
from xero.auth import OAuth2Credentials
from xero.constants import XeroScopes

def url_to_file_guid(url_id):
    """Return the guid from the URL id

    :param str url_id: the url id parameter to convert
    :return: the guid
    :rtype: str
    """

    return "{}-{}-{}-{}-{}".format(url_id[0:8], url_id[8:12], url_id[12:16], url_id[16:20], url_id[20:])


def get_file_guid(file):
    """Return the guid of the file

    :param api.models.FileUpload file: the fileUpload model instance
    :return: the guid
    :rtype: str
    """

    try:
        return str(file.url_guid).replace('-', '')
    except FileUpload.DoesNotExist:
        return ''


def get_file_url(url_path, parent_dir='/uploads/', strict=False):
    return url_path


def add_to_header(response, key, value):
    if response.has_header(key):
        values = re.split(r'\s*,\s*', response[key])

        if value not in values:
            response[key] = ', '.join(values + [value])
    else:
        response[key] = value


def docker_status(request):
    return HttpResponse("OK")


def home(request):
    context = {
        'title': settings.APP_NAME,
        'redirect_url': '/static/dev_index.html' if getattr(settings, 'DEV_MODE', False) else '/static/index.html'
    }
    response = render(request, 'index.html', context)
    add_to_header(response, 'Cache-Control', 'no-cache')
    add_to_header(response, 'Cache-Control', 'max-age=0')
    add_to_header(response, 'Expires', '0')
    add_to_header(response, 'Expires', 'Tue, 01 Jan 1980 1:00:00 GMT')
    add_to_header(response, 'Pragma', 'no-cache')
    return response


def fetch_new_mails(request):
    all_mailbox = Mailbox.objects.all()
    message = ""
    count = 0

    for mailbox in all_mailbox:
        try:
            new_mail = mailbox.get_new_mail()
            count += len(new_mail)
        except AttributeError:
            message += "No mailbox available.\n"

    return JsonResponse({
        'success': True,
        'message': message,
        'count': count,
    })


class SendEmailAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JSONWebTokenParamAuthentication,]

    def post(self, request, *args, **kwargs):
        try:

            data = request.data
            message = data.get('body', '')
            links = data.get('links', [])


            toAddresses = [x.strip() for x in data['to'].split(',')]  # handles if there is a , to send multiples

            print("Sending email to " + ", ".join(to for to in toAddresses))

            html_message = message
            if data['from']:
                html_message += "<br/><br/>This message was sent to you from the Cormack JMS app on behalf of " + data['from'] + "."
                message += "\n\nThis message was sent to you from the Cormack JMS app on behalf of " + data["from"] + "."
            else:
                html_message += "<br/><br/>This message was sent to you from the Cormack JMS app."
                message += "\n\nThis message was sent to you from the Cormack JMS app."

            if len(links) > 0:

                html_message += '<br /><br />Links:'
                message += '\n\nLinks:'

                for link_file in links:
                    file = FileUpload.objects.get(id=link_file['id'])
                    the_url = request.build_absolute_uri(
                        reverse('redirectoriginal', kwargs={'file_id': get_file_guid(file)})).replace('/usr/src/app', '')
                    message += '\n' + the_url + '\n'
                    html_message += '<br /><a href="{}">{}</a>'.format(the_url, link_file['name'])

                html_message += '<br />-- Total {} files --'.format(len(links))
                message += '\n-- Total {} files --'.format(len(links))
            else:
                html_message = message
            
            # Removed due to an urgent need to get email working on 9 Jan 2020.
            # Office 365 started rejecting emails not from the user you are logged in as.
            #
            #send_mail(data['subject'], message, data['from'], toAddresses, fail_silently=False, html_message=html_message)
            email = EmailMultiAlternatives(
                subject=data['subject'],
                body=message,
                from_email='jms@cormackgroup.com.au', # TODO: Don't hard-code this.
                to=toAddresses)
            email.attach_alternative(html_message, "text/html")
            email.send()

            return response.Response("OK")
        except e as Exception:
            print("Exception when trying to send an email: " + str(e))


def redirect_original(request, file_id):
    if request.method == 'GET':
        guid = url_to_file_guid(file_id)

        try:
            UUID(guid, version=4)
        except ValueError:
            # If it's a value error, then the string
            # is not a valid hex code for a UUID.
            return HttpResponseBadRequest("Invalid file.")

        file = FileUpload.objects.get(url_guid=guid)
        if file:
            return HttpResponseRedirect("/media/%s"%file.file)
        else:
            return HttpResponseBadRequest("Invalid file.")


def redirect_notification(request, url_id):
    if request.method == 'GET':
        guid = url_to_file_guid(url_id)

        try:
            UUID(guid, version=4)
        except ValueError:
            # If it's a value error, then the string
            # is not a valid hex code for a UUID.
            return HttpResponseBadRequest("Invalid notification.")

        notification = JobNotification.objects.get(guid=guid)

        if not notification:
            return HttpResponseBadRequest("Invalid notification.")

        job = notification.job_set.first()

        if not job:
            return HttpResponseBadRequest("Invalid notification.")

        protocol = 'https://' if request.is_secure() else 'http://'
        redirect_url = '{}{}/static/index.html#/job/edit/{}'.format(protocol, request.META['HTTP_HOST'], job.id)
        return HttpResponseRedirect(redirect_url)


class DownloadInvoice(APIView):
    authentication_classes = (JSONWebTokenParamAuthentication, SessionAuthentication,)

    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def get(self, request, format=None, id=None):
        xero = connectToXero()

        entity = XeroEntity.objects.get(pk=id)
        # noinspection PyUnresolvedReferences
        invoice = xero.invoices.get(entity.xero_id, headers={'Accept': 'application/pdf'})

        response = HttpResponse(invoice, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice_%s.pdf"' % entity.xero_code
        return response


class DownloadPurchaseOrder(APIView):
    authentication_classes = (JSONWebTokenParamAuthentication, SessionAuthentication,)

    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def get(self, request, format=None, id=None):
        xero = connectToXero()

        entity = XeroEntity.objects.get(pk=id)
        # noinspection PyUnresolvedReferences
        invoice = xero.purchaseorders.get(entity.xero_id, headers={'Accept': 'application/pdf'})

        response = HttpResponse(invoice, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Purchase_Order_%s.pdf"' % entity.xero_code
        return response


class CreateJobInvoiceView(APIView):
    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def get(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def post(self, request, format=None):

        job = Job.objects.get(pk=request.data['id'])
        
        invoice = createJobInvoice(job)
        
        return Response(XeroEntitySerializer(invoice).data)


class CreateRepairInvoiceView(APIView):
    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def get(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def post(self, request, format=None):
        repair = Repair.objects.get(pk=request.data['id'])

        invoice = createRepairInvoice(repair)

        return Response(XeroEntitySerializer(invoice).data)


class CreateJobPurchaseOrderView(APIView):
    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def get(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def post(self, request, format=None):
        job = Job.objects.get(pk=request.data['id'])

        po = createJobPurchaseOrder(job)

        return Response(XeroEntitySerializer(po).data)


class CreateRepairPurchaseOrderView(APIView):
    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def get(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # noinspection PyUnusedLocal,PyShadowingBuiltins,PyMethodMayBeStatic
    def post(self, request, format=None):
        repair = Repair.objects.get(pk=request.data['id'])

        po = createRepairPurchaseOrder(repair)

        return Response(XeroEntitySerializer(po).data)
######################################################
class XeroOAuth2CallbackView (View):
    """
    GET: /api/signin-redirect?code=XXX

    Once the user is authenticated with Xero, they will redirect back to this view with a code that we exchange for a
    connection token, which we then use to get a refresh token.
    """
    
    def get(self, request):
        try:
            """ Handle the get request. """
            print("XeroOAuth2CallbackView - START")
            cred_state = caches['default'].get('xero_creds')
            print("XeroOAuth2CallbackView - cred_state")
            credentials = OAuth2Credentials(**cred_state)
            print("XeroOAuth2CallbackView - credentials")
            auth_secret = request.get_raw_uri()
            print("XeroOAuth2CallbackView - auth_secret")
            auth_secret = auth_secret.replace("http:","https:")
            credentials.verify(auth_secret)
            credentials.set_default_tenant()
            caches['default'].set('xero_creds', credentials.state)
            #added after invoicing worked
            return HttpResponseRedirect("/static/index.html#")
        except Exception as e:
            print(e)
######################################################
