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

  constructor(private api: ApiService, private calendar: NgbCalendar, private parserFormatter: NgbDateParserFormatter) { }

  ngOnInit() {
     
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
