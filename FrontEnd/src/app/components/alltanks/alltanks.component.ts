import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from 'src/app/api.service';

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
	@Input() simulationflag: boolean;

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
		console.log($('#td1').toggleClass('transform-active'));
		$('#td1').toggleClass('transform');
		console.log('xdfgchjb');
	};
}
