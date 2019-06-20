import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { Router, NavigationExtras } from '@angular/router';

@Component({
	selector: 'app-runningoutput',
	templateUrl: './runningoutput.component.html',
	styleUrls: [ './runningoutput.component.css' ]
})
export class RunningoutputComponent implements OnInit {
	runningoutput = 0;
	buttonstatus = false;
	status;
	confirmflag = false;
	@Output() message = new EventEmitter();
	constructor(private api: ApiService, private router: Router) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.getrunningoutput();
			}
		});
	}

	ngOnInit() {}
	getrunningoutput = () => {
		this.api.GetRunningOutput().subscribe((data) => {
			this.runningoutput = data;
			console.table(this.runningoutput);
		});
	};
	getconfirm = () => {
		this.api.PostNextHourSelection('running').subscribe((data) => {
			this.status = data;
			this.api.sendConfirmStatus(true);
			console.table(this.status);
		});
	};
	confirmation() {
		this.confirmflag = true;
		this.message.emit(this.confirmflag);
		console.log('@@@@@@@@@@ inside bestfit @@@@@@@@@@@');
	}
	copy() {
		let parameter: NavigationExtras = {
			queryParams: {
				id: 'rn'
			}
		};
		this.router.navigate([ 'inputs' ], parameter);
	}
}
