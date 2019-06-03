import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';


@Component({
  selector: 'app-bestfitoutput',
  templateUrl: './bestfitoutput.component.html',
  styleUrls: ['./bestfitoutput.component.css']
})
export class BestfitoutputComponent implements OnInit {
  bestfitoutput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getbestfitoutput  = () => {
    this.api.GetBestFitOutput().subscribe(
      data => {
        this.bestfitoutput = data;
        console.table(this.bestfitoutput)
      }
    )
}
}
