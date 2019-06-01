import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-tankno5',
  templateUrl: './tankno5.component.html',
  styleUrls: ['./tankno5.component.css']
})
export class Tankno5Component implements OnInit {
  qualityavg: any[] = [];
  qualityreal = 0;
  alltanks = 0;


  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  gettankinfo = () => {

    this.getqualityavg(5);
    this.getqualityreal(5);
    this.getclickedtank(5);
    this.api.sendSelection(5);

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
