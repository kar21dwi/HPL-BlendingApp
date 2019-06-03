import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-profitmaxinput',
  templateUrl: './profitmaxinput.component.html',
  styleUrls: ['./profitmaxinput.component.css']
})
export class ProfitmaxinputComponent implements OnInit {
  profitmaxinput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getprofitmaxinput = () => {
    this.api.GetProfitMaxInput().subscribe(
      data => {
        this.profitmaxinput = data;
        console.table(this.profitmaxinput)
      },
      error => {
          console.log(error)
      }
    )

  }

}
