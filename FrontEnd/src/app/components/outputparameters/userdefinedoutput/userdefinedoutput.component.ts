import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-userdefinedoutput',
	templateUrl: './userdefinedoutput.component.html',
	styleUrls: [ './userdefinedoutput.component.css' ]
})
export class UserdefinedoutputComponent implements OnInit {
	userdefinedoutput = 0;
	buttonstatus = false;
	status;
	confirmflag = false;
	barclick = 1;
	irotate = 0;

	@Output() message = new EventEmitter();

	constructor(private api: ApiService) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.getuserdefinedoutput();
			}
		});
	}

	ngOnInit() {}
	getuserdefinedoutput = () => {
		this.api.GetUserDefinedOutput().subscribe((data) => {
			this.userdefinedoutput = data;
			console.table(this.userdefinedoutput);
		});
	};
	getconfirm = () => {
		this.api.PostNextHourSelection('userdefined').subscribe((data) => {
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
