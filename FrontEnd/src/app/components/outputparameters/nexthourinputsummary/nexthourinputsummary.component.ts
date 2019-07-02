import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-nexthourinputsummary',
	templateUrl: './nexthourinputsummary.component.html',
	styleUrls: [ './nexthourinputsummary.component.css' ]
})
export class NexthourinputsummaryComponent implements OnInit {
	datafromnexthour = 0;
	buttonstatus = false;
	nexthourinput = 0;
	barclick = 1;
	irotate = 0;

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
