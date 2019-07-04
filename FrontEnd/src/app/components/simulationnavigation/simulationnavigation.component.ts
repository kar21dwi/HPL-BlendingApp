import { Component, OnInit, AfterViewChecked } from '@angular/core';
import { Routes, Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
	selector: 'app-simulationnavigation',
	templateUrl: './simulationnavigation.component.html',
	styleUrls: [ './simulationnavigation.component.css' ]
})
export class SimulationnavigationComponent implements OnInit, AfterViewChecked {
	currenturl;
	pagescompleted = [ 0, 0, 0 ];
	finalconfirm = false;
	scroll: any;

	constructor(private router: Router, private api: ApiService) {}

	ngOnInit() {
		this.api.getfinalconfirm.subscribe(
			(data) => {
				this.finalconfirm = data;
			},
			(error) => {
				console.log(error);
			}
		);
	}

	ngAfterViewChecked() {
		window.addEventListener('scroll', this.scroll, true);
		console.log(this.scroll);
		console.log(this.router.url);
		if (this.router.url == '/inputs') {
			console.log('zdxfgchbjklmrdtfygujioklrdtfyguhjikl;');
			this.pagescompleted[0] = 1;
		}
		if (this.router.url == '/outputs') {
			this.pagescompleted[1] = 1;
		}
	}
	backwardpage() {
		if (this.router.url == '/tanksdetails') {
			this.router.navigate([ '' ]);
		}
		if (this.router.url == '/inputs') {
			this.router.navigate([ 'tanksdetails' ]);
		}
		if (this.router.url == '/outputs') {
			this.router.navigate([ 'inputs' ]);
		}
	}
	forwardpage() {
		if (this.router.url == '/tanksdetails') {
			this.router.navigate([ 'inputs' ]);
		}
		if (this.router.url == '/inputs') {
			this.router.navigate([ 'outputs' ]);
		}
	}
}
