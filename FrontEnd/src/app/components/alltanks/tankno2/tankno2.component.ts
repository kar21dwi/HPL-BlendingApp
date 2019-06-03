import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
@Component({
  selector: 'app-tankno2',
  templateUrl: './tankno2.component.html',
  styleUrls: ['./tankno2.component.css']
})
export class Tankno2Component implements OnInit {
  qualityavg: any[] = [];
  qualityreal = 0;
  alltanks = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }

  gettankinfo = () => {

    this.getqualityavg(2);
    this.getqualityreal(2);
    this.getclickedtank(2);
    this.api.sendSelection(2);

  }

  getqualityavg = (i) => {
    this.api.GetQualityAvg(i).subscribe(
      data => {
        this.qualityavg = data;
        console.table(this.qualityavg)
      },
      error => {
          console.log(error)
      }
    )

  }

  getqualityreal = (i) => {
    this.api.GetQualityReal(i).subscribe(
      data => {
        this.qualityreal = data;
      },
      error => {
          console.log(error)
      }
    )
  }
  getclickedtank = (i) => {
    this.api.GetClickedTank(i).subscribe(
      data => {
        this.alltanks = data;
      },
      error => {
          console.log(error)
      }
    )
  }
 


}