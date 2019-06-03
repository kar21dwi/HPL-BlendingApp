import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import {NgbDateStruct, NgbCalendar} from '@ng-bootstrap/ng-bootstrap';
import {NgbDateParserFormatter} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-qualityquantity',
  templateUrl: './qualityquantity.component.html',
  styleUrls: ['./qualityquantity.component.css']
})
export class QualityquantityComponent implements OnInit {

  qualityquantitydata: any[] = [];
  fromdate: string;
  todate: string;
  model: NgbDateStruct;
  flag1 = false;
  flag2 = false;

  constructor(private api: ApiService, private calendar: NgbCalendar, private parserFormatter: NgbDateParserFormatter) { }

  ngOnInit() {
  }

  getqualityquantity = () => {
    this.api.GetQualityQuantity(this.fromdate , this.todate).subscribe(
     data => {
       this.qualityquantitydata = data;
       console.table(this.qualityquantitydata);
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
