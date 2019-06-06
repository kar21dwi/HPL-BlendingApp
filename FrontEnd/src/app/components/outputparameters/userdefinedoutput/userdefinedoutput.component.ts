import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-userdefinedoutput',
  templateUrl: './userdefinedoutput.component.html',
  styleUrls: ['./userdefinedoutput.component.css']
})
export class UserdefinedoutputComponent implements OnInit {
  userdefinedoutput = 0;
  buttonstatus = false;
  status;

  constructor(private api: ApiService) { 
    this.api.simulatebutton.subscribe(x => {
      this.buttonstatus = x
      if(this.buttonstatus){
        this.getuserdefinedoutput();
      }
        }
        )
  }

  ngOnInit() {
  }
  getuserdefinedoutput = () => {
    this.api.GetUserDefinedOutput().subscribe(data => {
        this.userdefinedoutput = data;
        console.table(this.userdefinedoutput)
        

      }
    )
    
}
getconfirm = ()=>{
  this.api.PostNextHourSelection('userdefined').subscribe(
    data => {
      this.status = data;
      this.api.sendConfirmStatus(true);
      console.table(this.status)
    }
  )

}
}
