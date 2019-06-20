import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import { Router, NavigationExtras } from '@angular/router';

@Component({
	selector: 'app-nexthouroutput',
	templateUrl: './nexthouroutput.component.html',
	styleUrls: [ './nexthouroutput.component.css' ]
})
export class NexthouroutputComponent implements OnInit {
	nexthouroutput = 0;
	buttonstatus = false;
	flag = true;
	confirm = false;

	constructor(private api: ApiService, private router: Router) {
		this.api.simulatebutton.subscribe((x) => {
			this.buttonstatus = x;
			if (this.buttonstatus) {
				this.getnexthouroutput();
			}
		});
	}

	ngOnInit() {
		this.api.confirmstatus.subscribe((data) => {
			this.confirm = data;
			if (this.confirm) {
				if (this.flag) {
					this.flag = true;
					this.api.GetNextHourOutput().subscribe(
						(data) => {
							this.nexthouroutput = data;
							console.table(this.nexthouroutput);
						},
						(error) => {
							console.log(error);
						}
					);
				}
			}
		});
	}
	getnexthouroutput = () => {
		this.api.GetNextHourOutput().subscribe((data) => {
			this.nexthouroutput = data;
			console.table(this.nexthouroutput);
		});
	};

	copy() {
		let parameter: NavigationExtras = {
			queryParams: {
				id: 'nh'
			}
		};
		this.router.navigate([ 'inputs' ], parameter);
	}
}
