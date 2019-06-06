import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';


@Component({
  selector: 'app-bestfitoutput',
  templateUrl: './bestfitoutput.component.html',
  styleUrls: ['./bestfitoutput.component.css']
})
export class BestfitoutputComponent implements OnInit {
  bestfitoutput = 0;
  buttonstatus = false;
  status;

  constructor(private api: ApiService) { 
    this.api.simulatebutton.subscribe(x => {
      this.buttonstatus = x
      if(this.buttonstatus){
        this.getbestfitoutput();
      }
        }
        )
  }

  ngOnInit() {
  }
  getbestfitoutput  = () => {
    this.api.GetBestFitOutput().subscribe(
      data => {
        this.bestfitoutput = data;
        console.table(this.bestfitoutput)
      }
    )
}
getconfirm = ()=>{
  this.api.PostNextHourSelection('bestfit').subscribe(
    data => {
      this.status = data;
      this.api.sendConfirmStatus(true);
      console.table(this.status)
    }
  )
  

}
}
