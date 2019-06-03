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
  tankselection = false;
  selectioncount = 0;

  constructor(private api: ApiService){
    this.api.getselectioncount.subscribe(x => {
    this.selectioncount = x
      }
      )
    this.buttondisable();
  }

  ngOnInit() {
  }

  gettankinfo = () => {

    this.getqualityavg(2);
    this.getqualityreal(2);
    this.getclickedtank(2);
    this.api.sendSelection(2);

    if (this.tankselection == false){ 
      this.tankselection = true;
      this.api.getselectioncount.subscribe(x => {
      this.selectioncount = x
      }
      )
       this.selectioncount = this.selectioncount + 1; 
      this.api.sendSelectionCount(this.selectioncount);
    }
    else {
    this.tankselection = false;
      this.api.getselectioncount.subscribe(x => {
      this.selectioncount = x
      }
      )
       this.selectioncount = this.selectioncount - 1; 
      this.api.sendSelectionCount(this.selectioncount);
    }


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
        console.table(this.qualityreal)
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
        console.table(this.alltanks)
      },
      error => {
          console.log(error)
      }
    )
  }
  buttondisable = () =>{
    if(this.selectioncount>=2 && this.tankselection == false)
    return true
    else
    return false

  }
 


}
