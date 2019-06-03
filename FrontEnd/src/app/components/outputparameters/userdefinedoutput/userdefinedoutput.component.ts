import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-userdefinedoutput',
  templateUrl: './userdefinedoutput.component.html',
  styleUrls: ['./userdefinedoutput.component.css']
})
export class UserdefinedoutputComponent implements OnInit {
  userdefinedoutput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getuserdefinedoutput = () => {
    this.api.GetUserDefinedOutput().subscribe(
      data => {
        this.userdefinedoutput = data;
        console.table(this.userdefinedoutput)
      }
    )
}
}
