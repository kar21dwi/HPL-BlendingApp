import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-profitmaxinputsummary',
	templateUrl: './profitmaxinputsummary.component.html',
	styleUrls: [ './profitmaxinputsummary.component.css' ]
})
export class ProfitmaxinputsummaryComponent implements OnInit {
	datafromprofitmax = 0;
	buttonstatus = false;
	profitmaxinput = 0;
	barclick = 1;
	irotate = 0;

	constructor(private api: ApiService) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.api.getprofitmaxinput.subscribe((x) => {
					this.profitmaxinput = x;
					console.table(this.profitmaxinput);
				});
			}
		});
	}

	ngOnInit() {}
	getprofitmaxinput = () => {};
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
