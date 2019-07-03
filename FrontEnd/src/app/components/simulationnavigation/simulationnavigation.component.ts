import { Component, OnInit, AfterViewChecked } from '@angular/core';
import { Routes, Router } from '@angular/router';

@Component({
	selector: 'app-simulationnavigation',
	templateUrl: './simulationnavigation.component.html',
	styleUrls: [ './simulationnavigation.component.css' ]
})
export class SimulationnavigationComponent implements OnInit, AfterViewChecked {
	currenturl;
	pagescompleted = [ 0, 0, 0 ];

	constructor(private router: Router) {}

	ngOnInit() {}

	ngAfterViewChecked() {
		console.log(this.router.url);
		if (this.router.url == '/inputs') {
			console.log('zdxfgchbjklmrdtfygujioklrdtfyguhjikl;');
			this.pagescompleted[0] = 1;
		}
		if (this.router.url == '/outputs') {
			this.pagescompleted[1] = 1;
		}
	}
}
