import { Directive, ElementRef, ChangeDetectorRef, Output, EventEmitter, Input } from '@angular/core';

import * as moment from "moment";
import * as $ from "jquery";
import * as datetimepicker from "eonasdan-bootstrap-datetimepicker";

@Directive({
    selector: '[appDatetimepicker]'
})
export class DatetimepickerDirective {

    /**
     * Whether to show the time picker as well.
     */
    @Input() datepickerShowTime : boolean = false;

    /**
     * The format to use.
     */
    @Input() datepickerFormat : string = null;

    /**
     * The change event.
     */
    @Output() change : EventEmitter<any> = new EventEmitter();

    constructor(
        private element : ElementRef,
        private changeDetector : ChangeDetectorRef,
    ) {}

    ngOnInit() {
        datetimepicker.call($(this.element.nativeElement), {
            format: this.datepickerFormat ?? (this.datepickerShowTime ? "YYYY-MM-DD[T]HH:mm:ss" : "YYYY-MM-DD"),
            timeZone: "Australia/Melbourne",
            stepping: 15
        });
        $(this.element.nativeElement).on("dp.change", (event : {date: Date, oldDate: Date}) => {
            console.log(`dp.change`, event.date, event.oldDate);
            if (event.date != event.oldDate && event.oldDate != null)
            {
                this.element.nativeElement.dispatchEvent(new Event("input"));
                this.changeDetector?.detectChanges()
                this.change.emit();
            }
        });
    }
}
