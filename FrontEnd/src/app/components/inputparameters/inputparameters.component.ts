import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-inputparameters',
  templateUrl: './inputparameters.component.html',
  styleUrls: ['./inputparameters.component.css']
})
export class InputparametersComponent implements OnInit {
  //givechildcomponents = 0;
   nextclicked= false;

  constructor(private api: ApiService) {
   }

  ngOnInit() {
  }
  giveinputs = () => {
    if(this.nextclicked == false) {
      this.nextclicked = true;
    }

  }
  givechild = () => {

  }
  


}
