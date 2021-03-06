import { Component, OnInit, Input, AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-profitmaxinput',
	templateUrl: './profitmaxinput.component.html',
	styleUrls: [ './profitmaxinput.component.css' ]
})
export class ProfitmaxinputComponent implements OnInit, AfterContentChecked {
	profitmaxinput = 0;
	profitmaxquality = 0;
	check = true;
	barclick = 0;
	irotate = 0;
	@Input() nextclicked: boolean;

	constructor(private api: ApiService) {}

	ngOnInit() {}
	ngAfterContentChecked() {
		this.getprofitmaxinput();
	}
	getprofitmaxinput = () => {
		if (this.nextclicked == true && this.check) {
			this.check = false;
			this.api.GetProfitMaxInput().subscribe(
				(data) => {
					this.profitmaxinput = data;
					this.api.sendProfitMaxInput(this.profitmaxinput);
					console.table(this.profitmaxinput);
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
