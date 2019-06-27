import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { range } from 'rxjs';

@Component({
	selector: 'app-alltanks',
	templateUrl: './alltanks.component.html',
	styleUrls: [ './alltanks.component.css' ]
})
export class AlltanksComponent implements OnInit {
	sbtank = 0;
	receivednaphtha = 0;
	alltankslevels = 0;
	flag = 0;
	hoverover = false;
	@Input() simulationflag: boolean;
	panelOpenState = false;
	barclick = [ 0, 0 ];
	clickstatus = false;
	level = [ 11000, 10000, 3000, 4000, 8700 ];
	weight = 12020;
	irotate = [ 0, 0 ];
	totallevel = 12500;
	percentlevel = [ 0, 0, 0, 0, 0 ];
	tankno = 0;

	constructor(private api: ApiService) {
		for (var i = 0; i < 5; i++) {
			this.percentlevel[i] = this.level[i] / this.totallevel * 100;
		}
		// this.getsuctionblending();
	}

	ngOnInit() {
		this.api.getmainpageclickconfirmation.subscribe(
			(data) => {
				this.flag = data;
			},
			(error) => {
				console.log(error);
			}
		);
	}
	gettanksoverallstatus = () => {
		this.getsuctionblending();
		this.getreceivingnaphtha();
		this.getalltanks();
	};

	getsuctionblending = () => {
		this.api.GetSuctionBlending().subscribe(
			(data) => {
				this.sbtank = data;
				console.table(this.sbtank);
			},
			(error) => {
				console.log(error);
			}
		);
	};

	getreceivingnaphtha = () => {
		this.api.GetReceivingNaphtha().subscribe(
			(data) => {
				this.receivednaphtha = data;
				console.table(this.receivednaphtha);
			},
			(error) => {
				console.log(error);
			}
		);
	};
	getalltanks = () => {
		this.api.GetAllTanks().subscribe(
			(data) => {
				this.alltankslevels = data;
				console.table(this.alltankslevels);
			},
			(error) => {
				console.log(error);
			}
		);
	};

	linkclick(i, j) {
		this.flag = i;
		this.tankno = j;
	}

	clickstatusfunc() {
		this.clickstatus = !this.clickstatus;
	}
	clickbar(i) {
		if (this.barclick[i] == 1) {
			this.barclick[i] = 0;
			this.irotate[i] = 0;
		} else {
			this.barclick[i] = 1;
			this.irotate[i] = 180;
		}
	}
}
