import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
	selector: 'app-tanksdetail',
	templateUrl: './tanksdetail.component.html',
	styleUrls: [ './tanksdetail.component.css' ]
})
export class TanksdetailComponent implements OnInit {
	constructor(private router: Router) {}

	ngOnInit() {}
	page3() {
		this.router.navigate([ 'inputs' ]);
	}
}
