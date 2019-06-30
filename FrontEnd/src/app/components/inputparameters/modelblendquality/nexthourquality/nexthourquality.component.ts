import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-nexthourquality',
	templateUrl: './nexthourquality.component.html',
	styleUrls: [ './nexthourquality.component.css' ]
})
export class NexthourqualityComponent implements OnInit {
	nexthourblendedquality = 0;
	nexthourquality = 0;
	barclick = 0;
	irotate = 0;

	constructor(private api: ApiService) {
		this.api.getnexthourinput.subscribe((x) => {
			this.nexthourquality = x;
			console.table(this.nexthourquality);
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
