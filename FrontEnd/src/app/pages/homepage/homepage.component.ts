import { Component, OnInit, AfterViewChecked, ChangeDetectorRef, AfterViewInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { Router } from '@angular/router';

@Component({
	selector: 'app-homepage',
	templateUrl: './homepage.component.html',
	styleUrls: [ './homepage.component.css' ]
})
export class HomepageComponent implements OnInit, AfterViewChecked {
	flag = false;
	simulateflag = false;
	showContent = false;

	constructor(private api: ApiService, private router: Router) {}

	ngOnInit() {}

	ngAfterViewChecked() {
		if (this.simulateflag) {
			setTimeout(() => (this.showContent = true), 150);
			if (this.showContent) {
				this.api.sendSimulateFlag(this.simulateflag);
				this.router.navigate([ 'tanksdetails' ]);
			}
		}
	}

	simulationpage(e) {
		this.simulateflag = true;
	}
}
