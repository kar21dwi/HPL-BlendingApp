import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-bestfitquality',
  templateUrl: './bestfitquality.component.html',
  styleUrls: ['./bestfitquality.component.css']
})
export class BestfitqualityComponent implements OnInit {

  bestfitblendedquality = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getblendquality = () => {

  }

}
