import { Component, OnInit, DoCheck } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import {NgbDateStruct, NgbCalendar} from '@ng-bootstrap/ng-bootstrap';
import {NgbDateParserFormatter} from '@ng-bootstrap/ng-bootstrap';
declare var $: any;


@Component({
  selector: 'app-newnaphtha',
  templateUrl: './newnaphtha.component.html',
  styleUrls: ['./newnaphtha.component.css']
})



export class NewnaphthaComponent implements OnInit, DoCheck {

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
  transferquantity: any[] = [0, 0, 0, 0, 0, 0];
  remainingnaphtha;
  docheckcheck = true;


  constructor(private api: ApiService, private calendar: NgbCalendar, private parserFormatter: NgbDateParserFormatter) {
    this.newnaphtha = { Transport_Type: '', Date_Transfer_From: '', Date_Transfer_To: '',
    HOJ: '', Load_Port: '', BL_Quantity: '', Shore_Quantity: '', Opening_Stock: null,
    Source: '', PCN_NCU: null, PCN_CPP: null, FGN_CPP: null, CBFS_CPP: null, Vessel_Name: '', Aromatics: null, Colour: null
    , Density: null, IN_IP_Ratio: null, Naphthene: null, Olefins: null, Paraffin: null, RVP: null, Sulfur: null, FBP: null, IBP: null};

    this.receivednaphtha = [];
    this.qualityavg = [];
    this.qualityreal = [];

  }


  ngOnInit() {



  }

  ngDoCheck()	{

    if (this.flag) {
      if (this.docheckcheck) {

      this.docheckcheck = false;

     

}

}

  }





  getthismonthdetail = () => {
    this.api.GetThisMonthDetail().subscribe(
     data => {
       this.thismonthplan = data;
       console.table(this.thismonthplan[0]);
     },
     error => {
         console.log(error);
     }
    );

   }

   getanymonthdetail = () => {
     this.api.GetAnyMonthDetail(this.fromdate , this.todate).subscribe(
      data => {
        this.anymonthdetail = data;
        console.table(this.anymonthdetail);
      },
      error => {
          console.log(error);
      }
     );

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
            x => { this.receivednaphtha = x;

                   this.remainingnaphtha = this.newnaphtha.Shore_Quantity;

               },
            error => {
              console.log(error);
            }


          );

        },
        error => {
          console.log(error);
        }

      );

    }
    getqualityavg = (i) => {
      this.api.GetQualityAvg(i).subscribe(
        data => {
          this.qualityavg = data;
          console.table(this.qualityavg);
         this.count = this.count + 1;
        },
        error => {
            console.log(error);
        }
      );

    }

    getqualityreal = (i) => {
      this.api.GetQualityReal(i).subscribe(
        data => {
          this.qualityreal = data;
          console.table(this.qualityreal);
          this.count = this.count + 1;
        },
        error => {
            console.log(error);
        }
      );
    }
    getalltankslevel = () => {
      this.api.GetAllTanks().subscribe(
        data => {
          this.alltankslevel = data;
          console.table(this.alltankslevel);
          this.count = this.count + 1;
        },
        error => {
            console.log(error);
        }
      );
    }
    getsuctionblending = () => {
      this.api.GetSuctionBlending().subscribe(
        data => {
          this.sbtank = data;
          console.table(this.sbtank);
          this.count = this.count + 1;  
        },
        error => {
            console.log(error);
        }
      );

    }
    getreceivingnaphtha = () => {
      this.api.GetReceivingNaphtha().subscribe(
        data => {
          this.receivingnaphtha = data;
          console.table(this.receivingnaphtha);

          this.count = this.count + 1;
        },
        error => {
            console.log(error);
        }
      );
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

   showcalender1() {

     this.flag1 = true;
     this.flag2 = false;
   }

   showcalender2() {

     this.flag2 = true;
     this.flag1 = false;
   }

   transfernaphthaquantity = () => {

    this.transferquantity[5] = this.firstreceivetank;

    this.api.TransferNaphthaQuantity(this.transferquantity).subscribe(
      data => {

        console.log(data);

      }

     );

    }


   updateremainingnaphtha() {

     if ((this.newnaphtha.Shore_Quantity - this.transferquantity.reduce((a, b) => a + b, 0)) < 0) {

       this.remainingnaphtha = 0;

      } 
  else {

      for (let j = 1; j < 6; j++) {
        $('#tank' + j + 'amt').prop('disabled', false);
        $('#tank' + j + 'first').prop('disabled', true);
     }

      this.remainingnaphtha = this.newnaphtha.Shore_Quantity - this.transferquantity.reduce((a, b) => a + b, 0);

      if (this.remainingnaphtha == 0) {
        let value;

        for (let j = 1; j < 6; j++) {

            value = parseInt($('#tank' + j + 'amt').val() , 10) || 0;

            if (value == 0) {
              $('#tank' + j + 'amt').prop('disabled', true);
            } else {
              $('#tank' + j + 'first').prop('disabled', false);
            }

      }


    }


   }

  }

  firsttank(i) {

    this.firstreceivetank = i;

    if ($('#confirmbutton').is(':disabled')) {


      for (let j = 1 ; j < 6 ; j++) {

        if (j != i) {
          $('#tank' + j + 'first').prop('disabled', true);
        }

        }
      $('#confirmbutton').prop('disabled', false);

    } else {

      let value;

      for (let j = 1 ; j < 6 ; j++) {

        value = parseInt($('#tank' + j + 'amt').val() , 10) || 0;

        if (value) {
          $('#tank' + j + 'first').prop('disabled', false);
        }

        }

      $('#confirmbutton').prop('disabled', true);


     }
 }

}
