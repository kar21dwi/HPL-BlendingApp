import { Component, OnInit, Input, HostListener } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-inputs',
  templateUrl: './inputs.component.html',
  styleUrls: ['./inputs.component.css']
})
export class InputsComponent implements OnInit {
  inputparameter = 0;
  blendratio ;
  inputud ;
  naphthaload ; lpgl; c5; c6; cot; pdi; pressure; nh;
  flag = false;


  @Input() suctiontank : any;
  @Input() blendingtank : any;

  constructor(private api: ApiService) { 
    this.inputud = { Suction_Tank_No_UD: '', Blending_Tank_No_UD: '', Blend_Ratio_UD: '',
                    Naphtha_Load_UD:'', LPG_Load_UD:'',C5_Load_UD:'', C6_Load_UD: '', Naphtha_Heater_UD: '',
                    COT_UD: '',GF_PDI_UD: '',Suc_Pressure_UD: ''};

     this.api.tabpressstatus.subscribe(x => {
      if (x){
       this.transferblendratio(); 
      }
     }
    )    
                    

  }

 
  ngOnInit() {
     
  }
  getselectedtanks = () => {
    


}
simulate = () =>{
  this.inputud.Suction_Tank_No_UD = this.suctiontank;
  this.inputud.Blending_Tank_No_UD = this.blendingtank;
  this.inputud.Blend_Ratio_UD = this.blendratio;
  this.inputud.Naphtha_Load_UD = this.naphthaload;
  this.inputud.LPG_Load_UD = this.lpgl;
  this.inputud.C5_Load_UD = this.c5;
  this.inputud.C6_Load_UD = this.c6;
  this.inputud.Naphtha_Heater_UD = this.nh;
  this.inputud.COT_UD = this.cot;
  this.inputud.GF_PDI_UD = this.pdi;
  this.inputud.Suc_Pressure_UD = this.pressure;

  this.api.PostUserDefinedInputs(this.inputud).subscribe(
    data => {
      this.flag = true;
      this.inputparameter = data;
      this.api.sendUserInput(this.inputud);
      this.api.sendSimulateButton(this.flag)
    },
    error => {
        console.log(error)
    }
  )

}


transferblendratio = () => {

  this.api.sendBlendRatio(this.blendratio);

}


}
