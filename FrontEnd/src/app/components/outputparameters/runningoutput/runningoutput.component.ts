import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-runningoutput',
  templateUrl: './runningoutput.component.html',
  styleUrls: ['./runningoutput.component.css']
})
export class RunningoutputComponent implements OnInit {
  runningoutput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getrunningoutput = () => {
    this.api.GetRunningOutput().subscribe(
      data => {
        this.runningoutput = data;
        console.table(this.runningoutput)
      }
    )
}

}
