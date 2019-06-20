import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-inputparameters',
	templateUrl: './inputparameters.component.html',
	styleUrls: [ './inputparameters.component.css' ]
})
export class InputparametersComponent implements OnInit {
	//givechildcomponents = 0;
	nextclicked = false;
	nextoutputclick = false;
	@Input() newud: any;

	constructor(private api: ApiService) {}

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
	giveinputs = () => {
		if (this.nextclicked == false) {
			this.nextclicked = true;
		}
	};
	givechild = () => {};
}
