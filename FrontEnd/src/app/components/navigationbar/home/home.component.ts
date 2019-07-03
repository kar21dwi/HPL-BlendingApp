import { Component, OnInit } from '@angular/core';
import { Routes, Router } from '@angular/router';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: [ './home.component.css' ]
})
export class HomeComponent implements OnInit {
	flag = true;

	constructor(private router: Router) {}

	ngOnInit() {
		console.log(this.router.url);
	}

	mainpage() {
		if (this.flag == false) {
			this.flag = true;
		} else {
			this.flag = false;
		}
	}
}
