import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';

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
	@Output() message = new EventEmitter();

	constructor(private api: ApiService) {
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
}
