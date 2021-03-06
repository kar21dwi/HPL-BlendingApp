import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-bestfitquality',
	templateUrl: './bestfitquality.component.html',
	styleUrls: [ './bestfitquality.component.css' ]
})
export class BestfitqualityComponent implements OnInit {
	bestfitblendedquality = 0;
	bestfitquality = 0;
	barclick = 0;
	irotate = 0;

	constructor(private api: ApiService) {
		this.api.getbestfitinput.subscribe((x) => {
			this.bestfitquality = x;
			console.table(this.bestfitquality);
		});
	}

	ngOnInit() {}
	getblendquality = () => {};
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
