import { Component, OnInit, AfterContentChecked } from '@angular/core';
import { ApiService } from './api.service';

//new line add

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: [ './app.component.css' ],
	providers: [ ApiService ]
})
export class AppComponent implements OnInit, AfterContentChecked {
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
		this.api.simulateflagstatus.subscribe(
			(data) => {
				console.log('*****************akfd;akwblsiu');

				this.simulationflag = data;
				console.log(this.simulationflag);
			},
			(error) => {
				console.log(error);
			}
		);
	}
	ngAfterContentChecked() {}
	closeblurwindow() {
		this.api.sendMainPageClickConfirmation(0);
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
