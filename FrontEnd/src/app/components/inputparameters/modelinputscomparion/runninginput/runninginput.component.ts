import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-runninginput',
  templateUrl: './runninginput.component.html',
  styleUrls: ['./runninginput.component.css']
})
export class RunninginputComponent implements OnInit {
  runninginput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getrunninginput = () => {
    this.api.GetRunningInput().subscribe(
      data => {
        this.runninginput = data;
        console.table(this.runninginput)
      },
      error => {
          console.log(error)
      }
    )

  }

}
