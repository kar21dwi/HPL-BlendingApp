import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-tankno3',
  templateUrl: './tankno3.component.html',
  styleUrls: ['./tankno3.component.css']
})
export class Tankno3Component implements OnInit {
  qualityavg: any[] = [];
  qualityreal = 0;
  alltanks = 0;


  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  gettankinfo = () => {

    this.getqualityavg(3);
    this.getqualityreal(3);
    this.getclickedtank(3);
    this.api.sendSelection(3);

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
