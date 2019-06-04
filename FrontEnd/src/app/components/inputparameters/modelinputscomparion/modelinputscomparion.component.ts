import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-modelinputscomparion',
  templateUrl: './modelinputscomparion.component.html',
  styleUrls: ['./modelinputscomparion.component.css']
})
export class ModelinputscomparionComponent implements OnInit {
  childcomponents = 0;
  @Input() nextclicked : boolean;

  constructor(private api: ApiService) { 
  }

  ngOnInit() {
  }
  givechildcomponents = () => {
    console.log(this.nextclicked)
  }

    

  

}
