import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-profitmaxquality',
	templateUrl: './profitmaxquality.component.html',
	styleUrls: [ './profitmaxquality.component.css' ]
})
export class ProfitmaxqualityComponent implements OnInit {
	profitmaxblendedquality = 0;
	profitmaxquality = 0;
	barclick = 0;
	irotate = 0;

	constructor(private api: ApiService) {
		this.api.getprofitmaxinput.subscribe((x) => {
			this.profitmaxquality = x;
			console.table(this.profitmaxquality);
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
