import { Component, OnInit, Input} from '@angular/core';

@Component({
  selector: 'app-blendquality',
  templateUrl: './blendquality.component.html',
  styleUrls: ['./blendquality.component.css']
})
export class BlendqualityComponent implements OnInit {
  blendedqualitycalculate = 0;
  @Input() qualityavgs = 0;
  @Input() qualityavgb = 0;
  @Input() qualityreals = 0;
  @Input() qualityrealb = 0;

  constructor() { }

  ngOnInit() {
  }
  calculateblendedquality = () => {

  }
}
