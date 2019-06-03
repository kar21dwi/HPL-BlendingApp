import { Component, OnInit, Input} from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-blendquality',
  templateUrl: './blendquality.component.html',
  styleUrls: ['./blendquality.component.css']
})
export class BlendqualityComponent implements OnInit {
  blendedqualitycalculate = 0;
  blendratio = 0;
  @Input() qualityavgs = 0;
  @Input() qualityavgb = 0;
  @Input() qualityreals = 0;
  @Input() qualityrealb = 0;

  constructor(private api: ApiService) { 
    console.log("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    console.log(this.blendratio)
    console.log("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    this.api.getblendratio.subscribe(x => {
    this.blendratio = x
      }
      )
  }

  ngOnInit() {
  }
  calculateblendedquality = () => {

  }
}
