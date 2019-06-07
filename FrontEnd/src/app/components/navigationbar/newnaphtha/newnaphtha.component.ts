import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import {NgbDateStruct, NgbCalendar} from '@ng-bootstrap/ng-bootstrap';
import {NgbDateParserFormatter} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-newnaphtha',
  templateUrl: './newnaphtha.component.html',
  styleUrls: ['./newnaphtha.component.css']
})
export class NewnaphthaComponent implements OnInit {

  thismonthplan;
  anymonthdetail: any[] = [];
  fromdate: string;
  todate: string;
  model: NgbDateStruct;
  flag1 = false;
  flag2 = false;
  flag = false;
  firstreceivetank;
  newnaphtha;
  qualityavg: any[][]; 
  qualityreal: any[][] ;
  alltankslevel ;
  sbtank;
  receivingnaphtha;
  receivednaphtha: any[][];
  count = 0;
  transferquantity: any[] = [0,0,0,0,0,0];
  remainingnaphtha;
  firsttankflag1 = false;
  firsttankflag2 = false;
  firsttankflag3 = false;
  firsttankflag4 = false;
  firsttankflag5 = false;
  buttondisableenabled = false

  constructor(private api: ApiService, private calendar: NgbCalendar, private parserFormatter: NgbDateParserFormatter) { 
    this.newnaphtha = { Transport_Type: '', Date_Transfer_From: '', Date_Transfer_To: '',
    HOJ:'', Load_Port:'',BL_Quantity:'', Shore_Quantity: '', Opening_Stock: null,
    Source: '',PCN_NCU: null,PCN_CPP: null,FGN_CPP: null,CBFS_CPP: null,Vessel_Name: '',Aromatics: null,Colour: null
    ,Density: null,IN_IP_Ratio: null,Naphthene: null,Olefins: null,Paraffin: null,RVP: null,Sulfur: null,FBP: null,IBP: null};
  
    this.receivednaphtha = [];
    this.qualityavg = [];
    this.qualityreal = [];
    this.remainingnaphtha = 0;
  

    
  }

 


  ngOnInit() {
  }

  getthismonthdetail = () => {
    this.api.GetThisMonthDetail().subscribe(
     data => {
       this.thismonthplan = data;
       console.table(this.thismonthplan[0]);
     },
     error => {
         console.log(error)
     }     
    )
  
   }
 
   getanymonthdetail = () => {
     this.api.GetAnyMonthDetail(this.fromdate , this.todate).subscribe(
      data => {
        this.anymonthdetail = data;
        console.table(this.anymonthdetail);
      },
      error => {
          console.log(error)
      }     
     )
   
    }


    postnewnaphthadetails = () => {
      this.api.PostNewNaphthaDetails(this.newnaphtha).subscribe(
        data => {
                    
                 this.getqualityreal(0); 
                 this.getqualityavg(0);       
                 this.getalltankslevel();       
                 this.getsuctionblending();     
                 this.getreceivingnaphtha();
                   

          this.api.GetReceivedNaphtha().subscribe(
            x => { this.receivednaphtha = x
                console.log(x)
                this.remainingnaphtha = this.newnaphtha.Shore_Quantity;         
            },
            error => {
              console.log(error)
            }

            
          )
         
        },
        error => {
          console.log(error)
        }
        
      )

    }
    getqualityavg = (i) => {
      this.api.GetQualityAvg(i).subscribe(
        data => {
          this.qualityavg = data;
          console.table(this.qualityavg)
          
        },
        error => {
            console.log(error)
        }
      )
  
    }
  
    getqualityreal = (i) => {
      this.api.GetQualityReal(i).subscribe(
        data => {
          this.qualityreal = data;
          console.table(this.qualityreal)
          
        },
        error => {
            console.log(error)
        }
      )
    }
    getalltankslevel = () => {
      this.api.GetAllTanks().subscribe(
        data => {
          this.alltankslevel = data;
          console.table(this.alltankslevel)
          
        },
        error => {
            console.log(error)
        }
      )
    }
    getsuctionblending = () => {
      this.api.GetSuctionBlending().subscribe(
        data => {
          this.sbtank = data;
          console.table(this.sbtank)
          this.flag = true
        },
        error => {
            console.log(error)
        }
      )
  
    }
    getreceivingnaphtha = () => {
      this.api.GetReceivingNaphtha().subscribe(
        data => {
          this.receivingnaphtha = data;
          console.table(this.receivingnaphtha)
         
          
        },
        error => {
            console.log(error)
        }
      )
    }
    
 
    onFromDateSelect($event) {
 
      this.fromdate = this.parserFormatter.format($event);
      console.log(this.fromdate);
      this.flag1 = false;
      
    }
 
    onToDateSelect($event) {
      
     this.todate = this.parserFormatter.format($event);
     console.log(this.todate);
     this.flag2 = false;
     
   }
 
   showcalender1(){
 
     this.flag1 = true;
     this.flag2 = false;
   }
 
   showcalender2(){
 
     this.flag2 = true;
     this.flag1 = false;
   } 
   transfernaphthaquantity = ()=>{

    this.transferquantity[5] = this.firstreceivetank

    this.api.TransferNaphthaQuantity(this.transferquantity).subscribe(
      data => {
      }

     )

    }
   firsttank = (i) =>{

     this.firstreceivetank = i;
     
     if (i==1)
     {
      if (this.firsttankflag1)
      {
        this.firsttankflag1 = false;
        
      }
      else{
        this.firsttankflag1 = true;
      }
      this.buttondisable();
      
      
     }
     
     if (i==2)
     {
      if (this.firsttankflag2)
      {
        this.firsttankflag2 = false;
        
      }
      else{
        this.firsttankflag2 = true;
      }
      this.buttondisable();
      
     }
     
     if (i==3)
     {
      if (this.firsttankflag3)
      {
        this.firsttankflag3 = false;
        
      }
      else{
        this.firsttankflag3 = true;
      }
      this.buttondisable();
      
     }
     
     if (i==4){
      if (this.firsttankflag4)
      {
        this.firsttankflag4 = false;
        
      }
      else{
        this.firsttankflag4 = true;
      }
      this.buttondisable();
      
     }
     
     if (i==5){
      if (this.firsttankflag5)
      {
        this.firsttankflag5 = false;
        
      }
      else{
        this.firsttankflag5 = true;
      }
      this.buttondisable();
      
     }
     
    
   }

   buttondisable() {
     if (this.buttondisableenabled){
      this.buttondisableenabled = false;
     }
     else{
      this.buttondisableenabled = true;
     }
     
     
     this.buttondisable1();
     this.buttondisable2();
     this.buttondisable3();
     this.buttondisable4();
     this.buttondisable5();
   }

   buttondisable1() {
     if (this.remainingnaphtha > 0) {
       return true
     }
     else if(this.buttondisableenabled && !(this.firsttankflag1)){
       return true
     }
     else {
       return false
     }
   }

   buttondisable2() {
    if (this.remainingnaphtha > 0) {
      return true
    }
    else if(this.buttondisableenabled && !(this.firsttankflag2)){
      return true
    }
    else  {
      return false
    }
  }

  buttondisable3() {
    if (this.remainingnaphtha > 0) {
      return true
    }
    else if(this.buttondisableenabled && !(this.firsttankflag3)){
      return true
    }
    else  {
      return false
    }
  }

  buttondisable4() {
    if (this.remainingnaphtha > 0) {
      return true
    }
    else if(this.buttondisableenabled && !(this.firsttankflag4)){
      return true
    }
    else {
      return false
    }
  }

  buttondisable5() {
    if (this.remainingnaphtha > 0) {
      return true
    }
    else if(this.buttondisableenabled && !(this.firsttankflag5)){
      return true
    }
    else {
      return false
    }
  }

  confirmation() {
    
    if (this.firsttankflag1 || this.firsttankflag2 || this.firsttankflag3 || this.firsttankflag4 || this.firsttankflag5){
      return false
    }
    else{
      return true
    }
  }

   updateremainingnaphtha() {

    console.log(this.receivingnaphtha)
    console.log(this.transferquantity.reduce((a, b) => a + b, 0))
    this.remainingnaphtha = this.newnaphtha.Shore_Quantity - this.transferquantity.reduce((a, b) => a + b, 0)

   }

   fielddisable1() {
     if (this.remainingnaphtha <= 0 && this.transferquantity[0] == 0){
      return true;
     }
     else{
       return false
     }
     
   }

   fielddisable2() {
    if (this.remainingnaphtha <= 0 && this.transferquantity[1] == 0){
     return true;
    }
    else{
      return false
    }
    
  }

  fielddisable3() {
    if (this.remainingnaphtha <= 0 && this.transferquantity[2] == 0){
     return true;
    }
    else{
      return false
    }
    
  }

  fielddisable4() {
    if (this.remainingnaphtha <= 0 && this.transferquantity[3] == 0){
     return true;
    }
    else{
      return false
    }
    
  }

  fielddisable5() {
    if (this.remainingnaphtha <= 0 && this.transferquantity[4] == 0){
     return true;
    }
    else{
      return false
    }
    
  }

}
