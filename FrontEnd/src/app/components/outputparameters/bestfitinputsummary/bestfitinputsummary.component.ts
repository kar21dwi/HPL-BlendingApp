import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-bestfitinputsummary',
	templateUrl: './bestfitinputsummary.component.html',
	styleUrls: [ './bestfitinputsummary.component.css' ]
})
export class BestfitinputsummaryComponent implements OnInit {
	datafrombestfit = 0;
	buttonstatus = false;
	bestfitinput = 0;
	barclick = 1;
	irotate = 0;

	constructor(private api: ApiService) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.api.getbestfitinput.subscribe((x) => {
					this.bestfitinput = x;
					console.table(this.bestfitinput);
				});
			}
		});
	}

	ngOnInit() {}
	getbestfitinput = () => {};
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
