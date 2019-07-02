import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { ActivatedRoute, Router, NavigationExtras } from '@angular/router';

@Component({
	selector: 'app-profitmaxoutput',
	templateUrl: './profitmaxoutput.component.html',
	styleUrls: [ './profitmaxoutput.component.css' ]
})
export class ProfitmaxoutputComponent implements OnInit {
	profitmaxoutput = 0;
	buttonstatus = false;
	status;
	confirmflag = false;
	barclick = 1;
	irotate = 0;
	@Output() message = new EventEmitter();

	constructor(private api: ApiService, private router: Router) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.getprofitmaxoutput();
			}
		});
	}

	ngOnInit() {}
	getprofitmaxoutput = () => {
		this.api.GetProfitMaxOutput().subscribe((data) => {
			this.profitmaxoutput = data;
			console.table(this.profitmaxoutput);
		});
	};
	getconfirm = () => {
		this.api.PostNextHourSelection('profitmax').subscribe((data) => {
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
				id: 'pm'
			}
		};
		this.router.navigate([ 'inputs' ], parameter);
	}
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
