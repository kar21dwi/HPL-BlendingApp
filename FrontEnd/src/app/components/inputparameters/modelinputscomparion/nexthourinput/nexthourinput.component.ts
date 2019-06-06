import { Component, OnInit, Input,AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';
@Component({
  selector: 'app-nexthourinput',
  templateUrl: './nexthourinput.component.html',
  styleUrls: ['./nexthourinput.component.css']
})
export class NexthourinputComponent implements OnInit,AfterContentChecked {
  nexthourinput = 0;
  check = true;
  flag = true;
  confirm = 0;
  @Input() nextclicked : boolean;

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.api.confirmstatus.subscribe(
      data => {
        this.confirm = data;
          if(this.confirm){ 
            if(this.flag) {
              this.flag = true;
              this.api.GetNextHourInput().subscribe(
                data => {
                  this.nexthourinput = data;
                  console.table(this.nexthourinput)
                  this.api.sendNextHourInput(this.nexthourinput);
                },
                error => {
                    console.log(error)
                }
              )
    
            }
         
          }
        
      }
    )
  }
  ngAfterContentChecked(){
    this.getnexthourinput();
    
      

    }
  getnexthourinput = () => {
    if(this.nextclicked == true && this.check){
      this.check = false;
    this.api.GetNextHourInput().subscribe(
      data => {
        this.nexthourinput = data;
        console.table(this.nexthourinput)
        this.api.sendNextHourInput(this.nexthourinput);
      },
      error => {
          console.log(error)
      }
    )

  }

}
}
