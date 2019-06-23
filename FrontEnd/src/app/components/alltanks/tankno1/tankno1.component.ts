import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-tankno1',
	templateUrl: './tankno1.component.html',
	styleUrls: [ './tankno1.component.css' ]
})
export class Tankno1Component implements OnInit {
	qualityavg: any[] = [];
	qualityreal = 0;
	alltanks = 0;
	tankselection = false;
	selectioncount = 0;
	flag = false;
	rowselector;
	@Input() simulationflag: boolean;
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
		this.getqualityavg(1);
		this.getqualityreal(1);
		this.getclickedtank(1);
		this.api.sendSelection(1);

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
		$('#tank1info').toggleClass('transform-active');
	};

	showqualityavg = () => {
		console.log('ksjfgdkh');
		this.api.sendMainPageClickConfirmation(1);
	};
	showqualityreal = () => {
		console.log('sdhfjs');
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
