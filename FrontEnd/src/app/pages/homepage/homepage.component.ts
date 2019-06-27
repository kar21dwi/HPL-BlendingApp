import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { Router } from '@angular/router';

@Component({
	selector: 'app-homepage',
	templateUrl: './homepage.component.html',
	styleUrls: [ './homepage.component.css' ]
})
export class HomepageComponent implements OnInit {
	flag = false;
	simulateflag = false;

	constructor(private api: ApiService, private router: Router) {}

	ngOnInit() {}
	closeblurwindow() {
		this.api.sendMainPageClickConfirmation(0);
	}
	simulationpage() {
		//console.log('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');

		this.simulateflag = true;
		console.log(this.simulateflag);
		this.api.sendSimulateFlag(this.simulateflag);

		this.router.navigate([ 'tanksdetails' ]);
	}
}
