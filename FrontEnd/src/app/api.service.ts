import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class ApiService {

  private getselectionsource = new BehaviorSubject<any>(0);
  public getselection = this.getselectionsource.asObservable();

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-Type':'application/json'})

  constructor(private http: HttpClient) { 

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

    return this.http.get(this.baseurl + '/getAllTanks/', {headers: this.httpHeaders})
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

  sendSelection(message : any){
    this.getselectionsource.next(message);
  }
  

}
