import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-modelinputscomparion',
  templateUrl: './modelinputscomparion.component.html',
  styleUrls: ['./modelinputscomparion.component.css']
})
export class ModelinputscomparionComponent implements OnInit {
  childcomponents = 0;

  constructor(private api: ApiService) { 
    this.modelchildcomponents();
  }

  ngOnInit() {
  }
  modelchildcomponents = () => {}

    

  

}
