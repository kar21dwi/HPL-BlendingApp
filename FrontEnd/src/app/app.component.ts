import { Component } from '@angular/core';
import { ApiService } from './api.service';

//new line add

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: [ './app.component.css' ],
	providers: [ ApiService ]
})
export class AppComponent {
	tanks = [
		{
			id: '',
			Paraffin: '',
			Olefins: '',
			Aromatics: '',
			Napthene: '',
			INIP_Ratio: '',
			Density: '',
			Sulfur: '',
			IBP: '',
			FBP: '',
			Paraffin_R: '',
			Olefins_R: '',
			Density_R: '',
			Paraffin_NIR: '',
			Olefins_NIR: '',
			Density_NIR: '',
			Level: '',
			Weight: ''
		}
	];
	loginUserData = [ { id: '', Username: '', Password: '' } ];
	flag = 0;
	simulationflag = false;
	nextclickflag = false;
	nextoutputclick = false;
	confirmationflag = false;
	copyflag: any;

	constructor(private api: ApiService) {}

	ngOnInit() {
		this.api.getmainpageclickconfirmation.subscribe(
			(data) => {
				this.flag = data;
			},
			(error) => {
				console.log(error);
			}
		);
	}
	closeblurwindow() {
		this.api.sendMainPageClickConfirmation(0);
	}

	simulationpage() {
		this.simulationflag = true;
	}
	nextpage() {
		this.nextclickflag = true;
	}
	nextpageoutput() {
		this.nextoutputclick = true;
		this.api.sendnextoutputclickstatus(true);
	}
	receivemessage($event) {
		this.confirmationflag = $event;
		console.log(this.confirmationflag);
	}
	receivecopymessage($event) {
		console.log('ksjhfdkjshf');
		this.copyflag = $event;
		console.log(this.copyflag);
	}
}
