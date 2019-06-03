import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-modelblendquality',
  templateUrl: './modelblendquality.component.html',
  styleUrls: ['./modelblendquality.component.css']
})
export class ModelblendqualityComponent implements OnInit {
  nirblendquality = 0;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }

nirchildblendcomponents = () => {

}

}