import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-nirblendquality',
  templateUrl: './nirblendquality.component.html',
  styleUrls: ['./nirblendquality.component.css']
})
export class NirblendqualityComponent implements OnInit {
  nirmodel = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getnirmodel = () => {
    this.api.GetNirModel().subscribe(
      data => {
        this.nirmodel = data;
        console.table(this.nirmodel)
      },
      error => {
          console.log(error)
      }
    )

  }

}
