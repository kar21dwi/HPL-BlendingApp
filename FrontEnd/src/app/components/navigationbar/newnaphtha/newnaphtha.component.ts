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
  newnaphtha;

  constructor(private api: ApiService, private calendar: NgbCalendar, private parserFormatter: NgbDateParserFormatter) { 
    this.newnaphtha = { Transport_Type: '', Date_Transfer_From: '', Date_Transfer_To: '',
    HOJ:'', Load_Port:'',BL_Quantity:'', Shore_Quantity: '', Opening_Stock: '',
    Source: '',PCN_NCU: '',PCN_CPP: '',FGN_CPP: '',CBFS_CPP_NCU: '',Vessel_Name: '',Aromatics: '',Colour: ''
    ,Density: '',IN_IP_Ratio: '',Naphthene: '',Olefins: '',Paraffin: '',RVP: '',Sulfur: '',FBP: '',IBP: ''};
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

}
