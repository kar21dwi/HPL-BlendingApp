import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-runningquality',
  templateUrl: './runningquality.component.html',
  styleUrls: ['./runningquality.component.css']
})
export class RunningqualityComponent implements OnInit {

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getblendquality = () => {

  }


}
