import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-runninginputsummary',
  templateUrl: './runninginputsummary.component.html',
  styleUrls: ['./runninginputsummary.component.css']
})
export class RunninginputsummaryComponent implements OnInit {
  dataandblendquality = 0;
  runninginput: any[] = [];
  buttonstatus = false;


  constructor(private api: ApiService) { 
    this.runninginput[0] = {Aromatics_RN:'', C5_Load_RN:'', C6_Load_RN : '',
    COT_RN :'', Density_RN: '', FBP_RN: '', GF_PDI_RN: '',
    IBP_RN: '', IN_IP_Ratio_RN:'', LPG_Load_RN: '', Naphtha_Heater_RN: '',
    Naphtha_Load_RN: '',Naphthene_RN: '', Olefins_RN: '', Paraffin_RN:'',
    Suc_Pressure_RN: '', Total_Load_RN:'', id: ''}
this.runninginput[1] = {Blend_Ratio_RN: '', Blending_Tank_No_RN:'', Suction_Tank_No_RN:''}


    this.api.simulatebutton.subscribe(x => {
      this.buttonstatus = x
      if(this.buttonstatus){
        this.api.getrunninginput.subscribe(x => {
          this.runninginput = x
          console.table(this.runninginput)
          
            }
            )
    
      
      }
        }
        )
  }

  ngOnInit() {
  }
  getrunninginput = () => {

  }
  

}
