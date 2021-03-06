import { Component, OnInit, Input, AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-runningquality',
	templateUrl: './runningquality.component.html',
	styleUrls: [ './runningquality.component.css' ]
})
export class RunningqualityComponent implements OnInit, AfterContentChecked {
	runningquality: any[] = [];
	@Input() nextclicked: boolean;
	check = true;
	receivedflag = false;
	barclick = 0;
	irotate = 0;

	constructor(private api: ApiService) {
		this.runningquality[0] = {
			Aromatics_RN: '',
			Density_RN: '',
			FBP_RN: '',
			IBP_RN: '',
			IN_IP_Ratio_RN: '',
			Naphthene_RN: '',
			Olefins_RN: '',
			Paraffin_RN: ''
		};

		this.runningquality[1] = { Blend_Ratio_RN: '', Blending_Tank_No_RN: '', Suction_Tank_No_RN: '' };
	}

	ngOnInit() {}
	ngAfterContentChecked() {
		if (this.check) {
			this.api.receivedvalue.subscribe((x) => {
				this.receivedflag = x;
				this.getblendquality();
			});
		}
	}

	getblendquality = () => {
		if (this.nextclicked == true && this.check && this.receivedflag) {
			this.check = false;
			this.api.getrunninginput.subscribe((x) => {
				this.runningquality = x;
				console.table(this.runningquality);
			});
		}
	};
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
