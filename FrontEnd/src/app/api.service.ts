import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class ApiService {

  private getselectionsource = new BehaviorSubject<any>(0);
  public getselection = this.getselectionsource.asObservable();

  private getselectioncountsource = new BehaviorSubject<any>(0);
  public getselectioncount = this.getselectioncountsource.asObservable();

  private getblendratiosource = new BehaviorSubject<any>(0);
  public getblendratio = this.getblendratiosource.asObservable();

 // private getmodelchildsource = new BehaviorSubject<any>(0);
  //public getchildcomponents = this.getmodelchildsource.asObservable();


  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-Type':'application/json'})

  constructor(private http: HttpClient) { 

  }

  GetQualityQuantity(fromdate, todate): Observable<any>{

    return this.http.get(this.baseurl + '/qualityquantity/' + fromdate + '/' + todate + '/',
     {headers: this.httpHeaders})
  }

  GetCredentialsCheck(username, password): Observable<any>{

    return this.http.get(this.baseurl + '/credentialscheck/' + username + '/' + password + '/',
     {headers: this.httpHeaders})
  }

  GetInputOutput(fromdate, todate): Observable<any>{

    return this.http.get(this.baseurl + '/inputoutput/' + fromdate + '/' + todate + '/',
     {headers: this.httpHeaders})
  }

  GetThisMonthDetail(): Observable<any>{

    return this.http.get(this.baseurl + '/thismonthdetail/', {headers: this.httpHeaders})
  }
  
  GetAnyMonthDetail(fromdate, todate): Observable<any>{

    return this.http.get(this.baseurl + '/anymonthdetail/' + fromdate + '/' + todate + '/',
     {headers: this.httpHeaders})
  } 

  GetComingMonthPlan(): Observable<any>{

    return this.http.get(this.baseurl + '/comingmonthplan/', {headers: this.httpHeaders})
  }

  GetAnyMonthPlan(fromdate, todate): Observable<any>{

    return this.http.get(this.baseurl + '/anymonthplan/' + fromdate + '/' + todate + '/',
     {headers: this.httpHeaders})
  }

  GetSuctionBlending() : Observable<any>{

    return this.http.get(this.baseurl + '/suctionblending/', {headers: this.httpHeaders})
  }
  GetReceivingNaphtha() : Observable<any>{

    return this.http.get(this.baseurl + '/receivingnaphtha/', {headers: this.httpHeaders})
  }
  GetAllTanks() : Observable<any>{

    return this.http.get(this.baseurl + '/alltanks/', {headers: this.httpHeaders})
  }
  GetQualityAvg(tankno) : Observable<any>{

    return this.http.get(this.baseurl + '/qualityavg/' + tankno + '/',
    {headers: this.httpHeaders})
  }
  GetQualityReal(tankno) : Observable<any>{

    return this.http.get(this.baseurl + '/qualityreal/'  + tankno + '/',
    {headers: this.httpHeaders})
  }
  GetClickedTank(tankno) : Observable<any>{

    return this.http.get(this.baseurl + '/clickedtank/'  + tankno + '/',
    {headers: this.httpHeaders})
  }
  PostUserDefinedInputs() : Observable<any>{

    return this.http.get(this.baseurl + '/userdefinedinputs/' ,
    {headers: this.httpHeaders})
  }
  GetRunningInput() : Observable<any>{

    return this.http.get(this.baseurl + '/runninginput/',
    {headers: this.httpHeaders})
  }
  GetProfitMaxInput() : Observable<any>{

    return this.http.get(this.baseurl + '/profitmaxinput/',
    {headers: this.httpHeaders})
  }
  GetBestFitInput() : Observable<any>{

    return this.http.get(this.baseurl + '/bestfitinput/',
    {headers: this.httpHeaders})
  }
  GetNextHourInput() : Observable<any>{

    return this.http.get(this.baseurl + '/nesthourinput/',
    {headers: this.httpHeaders})
  }
  GetNirActual() : Observable<any>{

    return this.http.get(this.baseurl + '/nirmodel/',
    {headers: this.httpHeaders})
  }
  GetNirModel() : Observable<any>{

    return this.http.get(this.baseurl + '/nirmodel/',
    {headers: this.httpHeaders})
  }
  GetUserDefinedOutput() : Observable<any>{

    return this.http.get(this.baseurl + '/userdefinedoutput/',
    {headers: this.httpHeaders})
  }
  GetRunningOutput() : Observable<any>{

    return this.http.get(this.baseurl + '/runningoutput/',
    {headers: this.httpHeaders})
  }
  GetProfitMaxOutput() : Observable<any>{

    return this.http.get(this.baseurl + '/profitmaxoutput/',
    {headers: this.httpHeaders})
  }
  GetBestFitOutput() : Observable<any>{

    return this.http.get(this.baseurl + '/bestfitoutput/',
    {headers: this.httpHeaders})
  }
  GetNextHourOutput() : Observable<any>{

    return this.http.get(this.baseurl + '/nexthouroutput/',
    {headers: this.httpHeaders})
  }


  sendSelection(message : any){
    this.getselectionsource.next(message);
  }
  sendSelectionCount(message : any){
    this.getselectioncountsource.next(message);
  }
  sendBlendRatio(message : any){
    this.getblendratiosource.next(message);
  }

 
  

}
