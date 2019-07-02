import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
	selector: 'app-outputparameters',
	templateUrl: './outputparameters.component.html',
	styleUrls: [ './outputparameters.component.css' ]
})
export class OutputparametersComponent implements OnInit {
	displaychildcomponents = 0;
	flag = false;
	@Output() message = new EventEmitter();
	@Output() copymessage = new EventEmitter();
	copyflag: any;
	barclick = 1;
	irotate = 0;

	constructor() {}

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
}
