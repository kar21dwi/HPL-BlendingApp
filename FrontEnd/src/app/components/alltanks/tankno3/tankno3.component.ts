import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-tankno3',
	templateUrl: './tankno3.component.html',
	styleUrls: [ './tankno3.component.css' ]
})
export class Tankno3Component implements OnInit {
	qualityavg: any[] = [];
	qualityreal = 0;
	alltanks = 0;
	tankselection = false;
	selectioncount = 0;
	@Input() simulationflag: boolean;
	@Input() qualityflag: 0;
	@Output() message = new EventEmitter();
	flag = false;
	rowselector;
	qualitylist: any[] = [ 10, 20, 30, 40 ];

	constructor(private api: ApiService) {
		this.api.getselectioncount.subscribe((x) => {
			this.selectioncount = x;
		});
		this.buttondisable();
	}

	ngOnInit() {
		this.api.getrowselectorstatus.subscribe((x) => {
			this.rowselector = x;
		});
	}
	gettankinfo = () => {
		this.getqualityavg(3);
		this.getqualityreal(3);
		this.getclickedtank(3);
		this.api.sendSelection(3);

		if (this.tankselection == false) {
			this.tankselection = true;
			this.api.getselectioncount.subscribe((x) => {
				this.selectioncount = x;
			});
			this.selectioncount = this.selectioncount + 1;
			this.api.sendSelectionCount(this.selectioncount);
		} else {
			this.tankselection = false;
			this.api.getselectioncount.subscribe((x) => {
				this.selectioncount = x;
			});
			this.selectioncount = this.selectioncount - 1;
			this.api.sendSelectionCount(this.selectioncount);
		}
	};

	getqualityavg = (i) => {
		this.api.GetQualityAvg(i).subscribe(
			(data) => {
				this.qualityavg = data;
				console.table(this.qualityavg);
			},
			(error) => {
				console.log(error);
			}
		);
	};

	getqualityreal = (i) => {
		this.api.GetQualityReal(i).subscribe(
			(data) => {
				this.qualityreal = data;
				console.table(this.qualityreal);
			},
			(error) => {
				console.log(error);
			}
		);
	};
	getclickedtank = (i) => {
		this.api.GetClickedTank(i).subscribe(
			(data) => {
				this.alltanks = data;
				console.table(this.alltanks);
			},
			(error) => {
				console.log(error);
			}
		);
	};

	buttondisable = () => {
		if (this.selectioncount >= 2 && this.tankselection == false) return true;
		else return false;
	};
	increaseheight = () => {
		this.flag = true;
		$('#tank3info').toggleClass('transform-active');
	};

	showqualityavg = () => {
		this.api.sendMainPageClickConfirmation(1);
	};
	showqualityreal = () => {
		this.api.sendMainPageClickConfirmation(2);
	};
	alertrow(i, event) {
		if (event.type == 'mouseenter') {
			this.api.sendRowSelectorStatus(i);
		} else {
			this.api.sendRowSelectorStatus(-1);
		}
	}
}
