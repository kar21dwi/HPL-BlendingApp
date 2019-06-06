import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import {NgbDateStruct, NgbCalendar} from '@ng-bootstrap/ng-bootstrap';
import {NgbDateParserFormatter} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-monthlyplanning',
  templateUrl: './monthlyplanning.component.html',
  styleUrls: ['./monthlyplanning.component.css']
})
export class MonthlyplanningComponent implements OnInit {

  comingmonthplan;
  anymonthplan: any[] = [];
  fromdate: string;
  todate: string;
  model: NgbDateStruct;
  flag1 = false;
  flag2 = false;
  outsideclick1 = false;
  outsideclick2 = false;
  monthplan;


  constructor(private api: ApiService, private calendar: NgbCalendar, private parserFormatter: NgbDateParserFormatter) {
    this.monthplan = { Date: '', Total_Stock: '', Usable_Stock: '',
    Source:'', Quantity:'',Budget_NCU_TPH:'', Actual_NCU_TPH: '', Actual_CPP_TPD: '',
    Budget_CPP_TPD: '',Draft_Level: ''}; 
  }
    
    
 
 
  ngOnInit() {
    
  }

  onClickedOutside1(e: Event) {
    if(this.flag1 && !(this.outsideclick1)) {
       this.outsideclick1 = true;
    }

  }

  onClickedOutside2(e: Event) {
    if(this.flag2 && !(this.outsideclick2)) {
       this.outsideclick2 = true;
    }

  }

  
  getcomingmonthplan = () => {
   this.api.GetComingMonthPlan().subscribe(
    data => {
      this.comingmonthplan = data;
      console.table(this.comingmonthplan);
    },
    error => {
        console.log(error)
    }     
   )
 
  }

  getanymonthplan = () => {
    this.api.GetAnyMonthPlan(this.fromdate , this.todate).subscribe(
     data => {
       this.anymonthplan = data;
       console.table(this.anymonthplan);
     },
     error => {
         console.log(error)
     }     
    )
  
   }
   postmonthplan  = () => {
    this.api.PostMonthPlan(this.monthplan).subscribe(
     data => {
       console.log(data);
     
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
    this.outsideclick1 = false;
    
  }

  showcalender2(){

    this.flag2 = true;
    this.flag1 = false;
    this.outsideclick2 = false;
  }

 
}
