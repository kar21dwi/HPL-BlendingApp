import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-bestfitinput',
  templateUrl: './bestfitinput.component.html',
  styleUrls: ['./bestfitinput.component.css']
})
export class BestfitinputComponent implements OnInit {
  bestfitinput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getbestfitinput = () => {
    this.api.GetBestFitInput().subscribe(
      data => {
        this.bestfitinput = data;
        console.table(this.bestfitinput)
      },
      error => {
          console.log(error)
      }
    )

  }

}
