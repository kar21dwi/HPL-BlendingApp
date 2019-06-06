import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-bestfitinputsummary',
  templateUrl: './bestfitinputsummary.component.html',
  styleUrls: ['./bestfitinputsummary.component.css']
})
export class BestfitinputsummaryComponent implements OnInit {
  datafrombestfit = 0;
  buttonstatus = false;
  bestfitinput = 0;
  
  constructor(private api: ApiService) {
    this.api.simulatebutton.subscribe(x => {
      this.buttonstatus = x
      if(this.buttonstatus){
        this.api.getbestfitinput.subscribe(x => {
          this.bestfitinput = x
          console.table(this.bestfitinput)
          
            }
            )
          
            
    
      
      }
        }
        )
   }

  ngOnInit() {
  }
  getbestfitinput = () => {

  }

}
