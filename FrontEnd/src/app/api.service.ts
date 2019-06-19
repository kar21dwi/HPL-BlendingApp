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

	private getrunninginputsource = new BehaviorSubject<any>(0);
	public getrunninginput = this.getrunninginputsource.asObservable();

	private getprofitmaxinputsource = new BehaviorSubject<any>(0);
	public getprofitmaxinput = this.getprofitmaxinputsource.asObservable();

	private getbestfitinputsource = new BehaviorSubject<any>(0);
	public getbestfitinput = this.getbestfitinputsource.asObservable();

	private getnexthourinputsource = new BehaviorSubject<any>(0);
	public getnexthourinput = this.getnexthourinputsource.asObservable();

	private receivedvaluesource = new BehaviorSubject<any>(0);
	public receivedvalue = this.receivedvaluesource.asObservable();

	private getuserinputssource = new BehaviorSubject<any>(0);
	public getuserinputs = this.getuserinputssource.asObservable();

	private getuserqualitysource = new BehaviorSubject<any>(0);
	public getuserquality = this.getuserqualitysource.asObservable();

	private simulatebuttonstatus = new BehaviorSubject<any>(0);
	public simulatebutton = this.simulatebuttonstatus.asObservable();

	private tabpressstatussource = new BehaviorSubject<any>(0);
	public tabpressstatus = this.tabpressstatussource.asObservable();

	private getconfirmsource = new BehaviorSubject<any>(0);
	public confirmstatus = this.getconfirmsource.asObservable();

	private getmainpageclickconfirmationsource = new BehaviorSubject<any>(0);
	public getmainpageclickconfirmation = this.getmainpageclickconfirmationsource.asObservable();

	private getnextoutputclickstatussource = new BehaviorSubject<any>(0);
	public getnextoutputclickstatus = this.getnextoutputclickstatussource.asObservable();

	// private getmodelchildsource = new BehaviorSubject<any>(0);
	//public getchildcomponents = this.getmodelchildsource.asObservable();

	baseurl = 'http://127.0.0.1:8000';
	httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });

	constructor(private http: HttpClient) {}

	GetQualityQuantity(fromdate, todate): Observable<any> {
		return this.http.get(this.baseurl + '/qualityquantity/' + fromdate + '/' + todate + '/', {
			headers: this.httpHeaders
		});
	}

	GetCredentialsCheck(username, password): Observable<any> {
		return this.http.get(this.baseurl + '/credentialscheck/' + username + '/' + password + '/', {
			headers: this.httpHeaders
		});
	}

	GetInputOutput(fromdate, todate): Observable<any> {
		return this.http.get(this.baseurl + '/inputoutput/' + fromdate + '/' + todate + '/', {
			headers: this.httpHeaders
		});
	}

	GetThisMonthDetail(): Observable<any> {
		return this.http.get(this.baseurl + '/thismonthdetail/', { headers: this.httpHeaders });
	}

	GetAnyMonthDetail(fromdate, todate): Observable<any> {
		return this.http.get(this.baseurl + '/anymonthdetail/' + fromdate + '/' + todate + '/', {
			headers: this.httpHeaders
		});
	}

	GetComingMonthPlan(): Observable<any> {
		return this.http.get(this.baseurl + '/comingmonthplan/', { headers: this.httpHeaders });
	}

	GetAnyMonthPlan(fromdate, todate): Observable<any> {
		return this.http.get(this.baseurl + '/anymonthplan/' + fromdate + '/' + todate + '/', {
			headers: this.httpHeaders
		});
	}

	GetSuctionBlending(): Observable<any> {
		return this.http.get(this.baseurl + '/suctionblending/', { headers: this.httpHeaders });
	}
	GetReceivingNaphtha(): Observable<any> {
		return this.http.get(this.baseurl + '/receivingnaphtha/', { headers: this.httpHeaders });
	}
	GetAllTanks(): Observable<any> {
		return this.http.get(this.baseurl + '/alltanks/', { headers: this.httpHeaders });
	}
	GetQualityAvg(tankno): Observable<any> {
		return this.http.get(this.baseurl + '/qualityavg/' + tankno + '/', { headers: this.httpHeaders });
	}
	GetQualityReal(tankno): Observable<any> {
		return this.http.get(this.baseurl + '/qualityreal/' + tankno + '/', { headers: this.httpHeaders });
	}
	GetClickedTank(tankno): Observable<any> {
		return this.http.get(this.baseurl + '/clickedtank/' + tankno + '/', { headers: this.httpHeaders });
	}
	PostUserDefinedInputs(inputud): Observable<any> {
		return this.http.post(this.baseurl + '/userdefinedinputs/', inputud, { headers: this.httpHeaders });
	}
	PostMonthPlan(monthplan): Observable<any> {
		return this.http.post(this.baseurl + '/monthplan/', monthplan, { headers: this.httpHeaders });
	}
	PostNewNaphthaDetails(newnaphtha): Observable<any> {
		return this.http.post(this.baseurl + '/newnaphtha/', newnaphtha, { headers: this.httpHeaders });
	}
	GetRunningInput(): Observable<any> {
		return this.http.get(this.baseurl + '/runninginput/', { headers: this.httpHeaders });
	}
	GetProfitMaxInput(): Observable<any> {
		return this.http.get(this.baseurl + '/profitmaxinput/', { headers: this.httpHeaders });
	}
	GetBestFitInput(): Observable<any> {
		return this.http.get(this.baseurl + '/bestfitinput/', { headers: this.httpHeaders });
	}
	GetNextHourInput(): Observable<any> {
		return this.http.get(this.baseurl + '/nexthourinput/', { headers: this.httpHeaders });
	}
	GetNirActual(): Observable<any> {
		return this.http.get(this.baseurl + '/niractual/', { headers: this.httpHeaders });
	}
	GetNirModel(): Observable<any> {
		return this.http.get(this.baseurl + '/nirmodel/', { headers: this.httpHeaders });
	}
	GetUserDefinedOutput(): Observable<any> {
		return this.http.get(this.baseurl + '/userdefinedoutput/', { headers: this.httpHeaders });
	}
	GetRunningOutput(): Observable<any> {
		return this.http.get(this.baseurl + '/runningoutput/', { headers: this.httpHeaders });
	}
	GetProfitMaxOutput(): Observable<any> {
		return this.http.get(this.baseurl + '/profitmaxoutput/', { headers: this.httpHeaders });
	}
	GetBestFitOutput(): Observable<any> {
		return this.http.get(this.baseurl + '/bestfitoutput/', { headers: this.httpHeaders });
	}
	GetNextHourOutput(): Observable<any> {
		return this.http.get(this.baseurl + '/nexthouroutput/', { headers: this.httpHeaders });
	}
	PostNextHourSelection(selection): Observable<any> {
		return this.http.get(this.baseurl + '/nexthourselectionupdate/' + selection + '/', {
			headers: this.httpHeaders
		});
	}
	GetReceivedNaphtha(): Observable<any> {
		return this.http.get(this.baseurl + '/receivednaphtha/', { headers: this.httpHeaders });
	}

	TransferNaphthaQuantity(transfernaphtha): Observable<any> {
		return this.http.post(this.baseurl + '/transfernaphthaquantity/', transfernaphtha, {
			headers: this.httpHeaders
		});
	}

	sendSelection(message: any) {
		this.getselectionsource.next(message);
	}
	sendSelectionCount(message: any) {
		this.getselectioncountsource.next(message);
	}
	sendBlendRatio(message: any) {
		this.getblendratiosource.next(message);
	}
	sendRunningInput(message: any) {
		this.getrunninginputsource.next(message);
	}
	sendProfitMaxInput(message: any) {
		this.getprofitmaxinputsource.next(message);
	}
	sendBestFitInput(message: any) {
		this.getbestfitinputsource.next(message);
	}
	sendNextHourInput(message: any) {
		this.getnexthourinputsource.next(message);
	}
	Receivedvalue(message: any) {
		this.receivedvaluesource.next(message);
	}
	sendUserInput(message: any) {
		this.getuserinputssource.next(message);
	}
	sendUserQuality(message: any) {
		this.getuserqualitysource.next(message);
	}
	sendSimulateButton(message: any) {
		this.simulatebuttonstatus.next(message);
	}
	sendTabPressStatus(message: any) {
		this.tabpressstatussource.next(message);
	}
	sendConfirmStatus(message: any) {
		this.getconfirmsource.next(message);
	}
	sendMainPageClickConfirmation(message: any) {
		this.getmainpageclickconfirmationsource.next(message);
	}
	sendnextoutputclickstatus(message: any) {
		this.getnextoutputclickstatussource.next(message);
	}
}
