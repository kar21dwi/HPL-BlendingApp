import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = "http://127.0.0.1:8000";
  httpHeaders = new HttpHeaders({'Content-Type':'application/json'})

  constructor(private http: HttpClient) { }

  getAllTanks() : Observable<any>{
    return this.http.get(this.baseurl + '/tanks/',
    {headers: this.httpHeaders})
  }
  createlogin(loginUserData): Observable<any>{
    const body = {Username:loginUserData.Username, Password:loginUserData.Password}
    return this.http.post(this.baseurl + '/login/', body,
    {headers: this.httpHeaders});
   
  }
}
