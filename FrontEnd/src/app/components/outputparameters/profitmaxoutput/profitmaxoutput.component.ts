import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-profitmaxoutput',
  templateUrl: './profitmaxoutput.component.html',
  styleUrls: ['./profitmaxoutput.component.css']
})
export class ProfitmaxoutputComponent implements OnInit {
  profitmaxoutput = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getprofitmaxoutput  = () => {
    this.api.GetProfitMaxOutput().subscribe(
      data => {
        this.profitmaxoutput = data;
        console.table(this.profitmaxoutput)
      }
    )
}


}
