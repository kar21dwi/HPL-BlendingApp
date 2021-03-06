import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-userdefinedinputsummary',
	templateUrl: './userdefinedinputsummary.component.html',
	styleUrls: [ './userdefinedinputsummary.component.css' ]
})
export class UserdefinedinputsummaryComponent implements OnInit {
	udinputsummary = 0;
	blendquality = 0;
	userinputs = 0;
	userquality: any[] = [];
	barclick = 1;
	irotate = 0;

	constructor(private api: ApiService) {
		this.api.getuserinputs.subscribe((x) => {
			this.userinputs = x;
			this.api.getuserquality.subscribe((x) => {
				this.userquality = x;
			});
		});
	}

	ngOnInit() {}
	getinput = () => {};
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
