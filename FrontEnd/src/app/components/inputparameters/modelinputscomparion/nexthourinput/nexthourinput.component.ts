import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
@Component({
  selector: 'app-nexthourinput',
  templateUrl: './nexthourinput.component.html',
  styleUrls: ['./nexthourinput.component.css']
})
export class NexthourinputComponent implements OnInit {
  nexthourinput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getnexthourinput = () => {
    this.api.GetNextHourInput().subscribe(
      data => {
        this.nexthourinput = data;
        console.table(this.nexthourinput)
      },
      error => {
          console.log(error)
      }
    )

  }

}
