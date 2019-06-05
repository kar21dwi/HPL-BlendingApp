import { Component, OnInit, Input, AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-runninginput',
  templateUrl: './runninginput.component.html',
  styleUrls: ['./runninginput.component.css']
})
export class RunninginputComponent implements OnInit, AfterContentChecked {
  runninginput: any[] = [];
  check = true;
  buttonstatus = false;
  @Input() nextclicked : boolean;
  constructor(private api: ApiService) {
    

    this.runninginput[0] = {Aromatics_RN:'', C5_Load_RN:'', C6_Load_RN : '',
                             COT_RN :'', Density_RN: '', FBP_RN: '', GF_PDI_RN: '',
                             IBP_RN: '', IN_IP_Ratio_RN:'', LPG_Load_RN: '', Naphtha_Heater_RN: '',
                             Naphtha_Load_RN: '',Naphthene_RN: '', Olefins_RN: '', Paraffin_RN:'',
                             Suc_Pressure_RN: '', Total_Load_RN:'', id: ''}
    this.runninginput[1] = {Blend_Ratio_RN: '', Blending_Tank_No_RN:'', Suction_Tank_No_RN:''}

  }
  ngOnInit() {
  }
  ngAfterContentChecked(){
    this.getrunninginput();

    }
  getrunninginput = () => {
    
    if(this.nextclicked == true && this.check){
      this.check =false;
      this.api.GetRunningInput().subscribe(
        data => {
          this.runninginput = data;
          console.table(this.runninginput)
          this.api.sendRunningInput(this.runninginput);
          this.api.Receivedvalue(true);
          
        },
        error => {
            console.log(error)
        }
      )
    }
    

  }
  
  }

