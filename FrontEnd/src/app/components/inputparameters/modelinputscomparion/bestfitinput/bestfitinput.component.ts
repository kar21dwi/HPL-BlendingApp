import { Component, OnInit, Input, AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-bestfitinput',
	templateUrl: './bestfitinput.component.html',
	styleUrls: [ './bestfitinput.component.css' ]
})
export class BestfitinputComponent implements OnInit, AfterContentChecked {
	bestfitinput = 0;
	check = true;
	@Input() nextclicked: boolean;
	barclick = 0;
	irotate = 0;

	constructor(private api: ApiService) {
		console.log('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!');
		if (this.nextclicked) {
			console.log('##############################');
			this.getbestfitinput();
		}
	}

	ngOnInit() {}
	ngAfterContentChecked() {
		this.getbestfitinput();
	}
	getbestfitinput = () => {
		if (this.nextclicked == true && this.check) {
			this.check = false;
			this.api.GetBestFitInput().subscribe(
				(data) => {
					this.bestfitinput = data;
					console.table(this.bestfitinput);
					this.api.sendBestFitInput(this.bestfitinput);
				},
				(error) => {
					console.log(error);
				}
			);
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
