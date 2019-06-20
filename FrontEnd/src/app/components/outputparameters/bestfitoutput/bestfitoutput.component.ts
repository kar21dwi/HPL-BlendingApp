import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { ActivatedRoute, Router, NavigationExtras } from '@angular/router';

@Component({
	selector: 'app-bestfitoutput',
	templateUrl: './bestfitoutput.component.html',
	styleUrls: [ './bestfitoutput.component.css' ]
})
export class BestfitoutputComponent implements OnInit {
	bestfitoutput = 0;
	buttonstatus = false;
	status;
	confirmflag = false;
	copyflag = false;

	@Output() message = new EventEmitter();
	@Output() copymessage = new EventEmitter();

	constructor(private api: ApiService, private router: Router) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.getbestfitoutput();
			}
		});
	}

	ngOnInit() {}
	getbestfitoutput = () => {
		this.api.GetBestFitOutput().subscribe((data) => {
			this.bestfitoutput = data;
			console.table(this.bestfitoutput);
		});
	};
	getconfirm = () => {
		this.api.PostNextHourSelection('bestfit').subscribe((data) => {
			this.status = data;
			this.api.sendConfirmStatus(true);
			console.table(this.status);
		});
	};
	confirmation() {
		this.confirmflag = true;
		this.message.emit(this.confirmflag);
	}
	copy() {
		let parameter: NavigationExtras = {
			queryParams: {
				id: 'bf'
			}
		};
		this.router.navigate([ 'inputs' ], parameter);
	}
}
