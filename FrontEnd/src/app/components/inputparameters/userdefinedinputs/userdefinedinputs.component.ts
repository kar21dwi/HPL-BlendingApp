import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-userdefinedinputs',
  templateUrl: './userdefinedinputs.component.html',
  styleUrls: ['./userdefinedinputs.component.css']
})
export class UserdefinedinputsComponent implements OnInit {

  selection = 0;

  constructor(private api: ApiService) { 
    this.getselectedtanks();
  }

  ngOnInit() {
  }
  getselectedtanks = () => {
    this.api.getselection.subscribe(x => {
      this.selection = x;
    }

    )

  }


}
