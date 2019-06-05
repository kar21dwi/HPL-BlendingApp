import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';


@Component({
  selector: 'app-nexthouroutput',
  templateUrl: './nexthouroutput.component.html',
  styleUrls: ['./nexthouroutput.component.css']
})
export class NexthouroutputComponent implements OnInit {
  nexthouroutput = 0;
  buttonstatus = false;

  constructor(private api: ApiService) {
    this.api.simulatebutton.subscribe(x => {
      this.buttonstatus = x
      if(this.buttonstatus){
        this.getnexthouroutput();
      }
        }
        )
   }

  ngOnInit() {
  }
  getnexthouroutput  = () => {
    this.api.GetNextHourOutput().subscribe(
      data => {
        this.nexthouroutput = data;
        console.table(this.nexthouroutput)
      }
    )
}

}
