import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-tankno1',
  templateUrl: './tankno1.component.html',
  styleUrls: ['./tankno1.component.css']
})
export class Tankno1Component implements OnInit {

  qualityavg: any[] = [];
  qualityreal = 0;
  alltanks = 0;



  constructor(private api: ApiService) {
    
  }
  ngOnInit() {
  }
  
  gettankinfo = () => {

    this.getqualityavg(1);
    this.getqualityreal(1);
    this.getclickedtank(1);
    this.api.sendSelection(1);

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

