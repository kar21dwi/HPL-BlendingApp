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
	barclick = false;
	clickstatus = false;
	level = 6005;
	weight = 12020;
	irotate = 0;
	totallevel = 12500;
	percentlevel = this.level / this.totallevel * 100;

	constructor(private api: ApiService) {
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
	dropdown = () => {
		/*
		console.log($('#td1').toggleClass('transform-active'));
		$('#td1').toggleClass('transform');
		console.log('xdfgchjb');
*/

		const content = document.getElementById('accordion');

		if (content.style.maxHeight == '172px') {
			content.style.maxHeight = '44px';
		} else {
			content.style.maxHeight = '172px';
		}
	};

	linkclick(i) {
		this.flag = i;
		this.api.sendMainPageClickConfirmation(this.flag);
	}

	dropaccord() {
		const content = document.getElementById('accordion2');

		if (content.style.maxHeight == '172px') {
			content.style.maxHeight = '44px';
		} else {
			content.style.maxHeight = '172px';
		}
	}

	clickstatusfunc() {
		this.clickstatus = !this.clickstatus;
	}
	clickbar() {
		this.barclick = !this.barclick;
		if (this.irotate) {
			this.irotate = 0;
		} else {
			this.irotate = 180;
		}
	}
}
