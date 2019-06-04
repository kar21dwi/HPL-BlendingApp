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
  paraffin = 0;
  aromatics = 0;
  density = 0;
  inipratio = 0;
  olefins = 0;
  naphthene = 0;
  ibp = 0;
  fbp = 0;
  flag = false;
  qualityarray: any[] = [];
  @Input() qualityavgs : any;
  @Input() qualityavgb : any;
  @Input() qualityreals : any;
  @Input() qualityrealb : any;

  constructor(private api: ApiService) { 
    this.api.getblendratio.subscribe(x => {
    this.blendratio = x
    if(this.blendratio)
    {

      this.calculateblendedquality();
    }
    
      }
      )
    
      
  }

  ngOnInit() {
  }
  calculateblendedquality = () => {
    this.paraffin = this.blendratio*this.qualityreals.Paraffin_Real + (1- this.blendratio)*this.qualityrealb.Paraffin_Real;
    this.aromatics = this.blendratio*this.qualityreals.Aromatics_Real + (1- this.blendratio)*this.qualityrealb.Aromatics_Real;
    this.density = this.blendratio*this.qualityreals.Density_Real + (1- this.blendratio)*this.qualityrealb.Density_Real;
    this.inipratio = this.blendratio*this.qualityreals.IN_IP_Ratio_Real + (1- this.blendratio)*this.qualityrealb.IN_IP_Ratio_Real;
    this.olefins = this.blendratio*this.qualityavgs.Olefins + (1- this.blendratio)*this.qualityavgb.Olefins;
    this.naphthene = this.blendratio*this.qualityavgs.Naphthene + (1- this.blendratio)*this.qualityavgb.Naphthene;
    this.ibp = this.blendratio*this.qualityavgs.IBP + (1- this.blendratio)*this.qualityavgb.IBP;
    this.fbp = this.blendratio*this.qualityavgs.FBP + (1- this.blendratio)*this.qualityavgb.FBP;
    this.qualityarray[0] = this.paraffin;
    this.qualityarray[1] = this.aromatics;
    this.qualityarray[2] = this.density;
    this.qualityarray[3] = this.inipratio;
    this.qualityarray[4] = this.olefins;
    this.qualityarray[5] = this.naphthene;
    this.qualityarray[6] = this.ibp;
    this.qualityarray[7] = this.fbp;

    this.api.sendUserQuality(this.qualityarray);
    
}
}
