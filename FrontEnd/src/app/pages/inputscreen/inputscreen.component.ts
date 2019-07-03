import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';

@Component({
	selector: 'app-inputscreen',
	templateUrl: './inputscreen.component.html',
	styleUrls: [ './inputscreen.component.css' ]
})
export class InputscreenComponent implements OnInit {
	newud: any;

	constructor(private route: ActivatedRoute, private router: Router) {}

	ngOnInit() {
		console.log(this.router.url);
		this.route.queryParams.subscribe((v) => {
			this.newud = v;
		});
	}
	page4() {
		this.router.navigate([ 'outputs' ]);
	}
}
