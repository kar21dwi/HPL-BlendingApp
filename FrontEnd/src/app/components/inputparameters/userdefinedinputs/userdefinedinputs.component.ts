import { Component, OnInit, Input, AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-userdefinedinputs',
	templateUrl: './userdefinedinputs.component.html',
	styleUrls: [ './userdefinedinputs.component.css' ]
})
export class UserdefinedinputsComponent implements OnInit, AfterContentChecked {
	suctiontank = 0;
	blendingtank = 0;
	suctiontankfinal = 0;
	blendingtankfinal = 0;
	count = 0;
	qualityavgs = 0;
	qualityavgb = 0;
	qualityreals = 0;
	qualityrealb = 0;
	check = true;
	@Input() nextclicked: boolean;
	nextoutputclick = false;

	constructor(private api: ApiService) {
		this.getselectedtanks();
	}

	ngOnInit() {
		this.api.getnextoutputclickstatus.subscribe(
			(data) => {
				this.nextoutputclick = data;
			},
			(error) => {
				console.log(error);
			}
		);
	}

	ngAfterContentChecked() {
		this.transferselection();
	}

	transferselection = () => {
		if (this.nextclicked == true && this.check) {
			this.suctiontankfinal = this.suctiontank;
			this.blendingtankfinal = this.blendingtank;
			console.log(this.nextclicked);

			if (this.count == 2 && this.check) {
				this.check = false;
				this.getqualityavg(this.suctiontank);
				this.getqualityreal(this.suctiontank);
				this.getqualityavg(this.blendingtank);
				this.getqualityreal(this.blendingtank);
			}
		}
	};

	getselectedtanks = () => {
		this.api.getselection.subscribe((x) => {
			if (this.nextclicked == true) {
				this.suctiontankfinal = this.suctiontank;
				this.blendingtankfinal = this.blendingtank;
				console.log(this.nextclicked);
			}
			if (this.suctiontank == x) {
				this.suctiontank = 0;
			} else if (this.blendingtank == x) {
				this.blendingtank = 0;
			} else if (this.suctiontank == 0) {
				this.suctiontank = x;
			} else if (this.blendingtank == 0) {
				this.blendingtank = x;
			}
		});
		this.api.getselectioncount.subscribe((x) => {
			this.count = x;
		});
	};
	getqualityavg = (i) => {
		this.api.GetQualityAvg(i).subscribe(
			(data) => {
				if (i == this.suctiontank) {
					this.qualityavgs = data;
					console.table(this.qualityavgs);
				} else {
					this.qualityavgb = data;
					console.table(this.qualityavgb);
				}
			},
			(error) => {
				console.log(error);
			}
		);
	};

	getqualityreal = (i) => {
		this.api.GetQualityReal(i).subscribe(
			(data) => {
				if (i == this.suctiontank) {
					this.qualityreals = data;
					console.table(this.qualityreals);
				} else {
					this.qualityrealb = data;
					console.table(this.qualityrealb);
				}
			},
			(error) => {
				console.log(error);
			}
		);
	};
}
