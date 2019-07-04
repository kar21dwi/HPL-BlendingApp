import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-outputparameters',
	templateUrl: './outputparameters.component.html',
	styleUrls: [ './outputparameters.component.css' ]
})
export class OutputparametersComponent implements OnInit {
	displaychildcomponents = 0;
	flag = false;
	confirmflag = false;
	@Output() message = new EventEmitter();
	@Output() copymessage = new EventEmitter();
	copyflag: any;
	barclick = 1;
	irotate = 0;
	comment;
	showContent = true;

	constructor(private api: ApiService) {}

	ngOnInit() {}
	displaychildcom = () => {};
	simulateoutput = () => {};

	receivemessage($event) {
		this.flag = $event;
		this.message.emit(this.flag);
	}

	receivecopymessage($event) {
		this.copyflag = $event;
		this.copymessage.emit(this.copyflag);
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

	savecomment() {
		this.confirmflag = true;
		this.api.sendFinalConfirmStatus(true);
		console.log('@@@@*************************&*%%^&#%@$' + this.showContent + 'skudglcuysafuodcs');
		setTimeout(() => (this.showContent = false), 8000);
		this.message.emit(false);
		console.log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' + this.showContent + 'skudglcuysafuodcs');
	}
}
