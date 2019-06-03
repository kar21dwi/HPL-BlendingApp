import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-profitmaxquality',
  templateUrl: './profitmaxquality.component.html',
  styleUrls: ['./profitmaxquality.component.css']
})
export class ProfitmaxqualityComponent implements OnInit {
  profitmaxblendedquality = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getblendquality = () => {

  }

}
