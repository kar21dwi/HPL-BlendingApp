import { Component, OnInit, Input, AfterViewChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-nexthourinputsummary',
	templateUrl: './nexthourinputsummary.component.html',
	styleUrls: [ './nexthourinputsummary.component.css' ]
})
export class NexthourinputsummaryComponent implements OnInit, AfterViewChecked {
	datafromnexthour = 0;
	buttonstatus = false;
	nexthourinput = 0;
	barclick = 1;
	irotate = 0;
	hideborder = false;
	@Input() confirmflag = false;

	constructor(private api: ApiService) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.api.getnexthourinput.subscribe((x) => {
					this.nexthourinput = x;
					console.table(this.nexthourinput);
				});
			}
		});
	}

	ngOnInit() {}

	ngAfterViewChecked() {
		if (this.confirmflag) {
			setTimeout(() => (this.hideborder = true), 8000);
		}
	}

	getnexthourinput = () => {};
	clickbar() {
		if (this.barclick == 1) {
			this.barclick = 0;
			this.irotate = 0;
		} else {
			this.barclick = 1;
			this.irotate = 180;
		}
	}
}
