import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-blendcomparison',
  templateUrl: './blendcomparison.component.html',
  styleUrls: ['./blendcomparison.component.css']
})
export class BlendcomparisonComponent implements OnInit {
  @Input() nextclicked : boolean;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  nirchildblendcomponents = () => {

  }

}
