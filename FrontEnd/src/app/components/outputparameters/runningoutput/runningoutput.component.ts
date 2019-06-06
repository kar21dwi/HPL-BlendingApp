import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-runningoutput',
  templateUrl: './runningoutput.component.html',
  styleUrls: ['./runningoutput.component.css']
})
export class RunningoutputComponent implements OnInit {
  runningoutput = 0;
  buttonstatus = false;
  status;

  constructor(private api: ApiService) {
    this.api.simulatebutton.subscribe(x => {
      this.buttonstatus = x
      if(this.buttonstatus){
        this.getrunningoutput();
      }
        }
        )
   }

  ngOnInit() {
  }
  getrunningoutput = () => {
    this.api.GetRunningOutput().subscribe(
      data => {
        this.runningoutput = data;
        console.table(this.runningoutput)
      }
    )
}
getconfirm = ()=>{
  this.api.PostNextHourSelection('running').subscribe(
    data => {
      this.status = data;
      this.api.sendConfirmStatus(true);
      console.table(this.status)
    }
  )

}

}
