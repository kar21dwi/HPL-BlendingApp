import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
@Component({
  selector: 'app-modelnirblendquality',
  templateUrl: './modelnirblendquality.component.html',
  styleUrls: ['./modelnirblendquality.component.css']
})
export class ModelnirblendqualityComponent implements OnInit {
  niractual = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getniractual = () => {
    this.api.GetNirActual().subscribe(
      data => {
        this.niractual = data;
        console.table(this.niractual)
      },
      error => {
          console.log(error)
      }
    )

  }

}
