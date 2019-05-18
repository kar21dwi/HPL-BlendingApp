import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  tanks = [{id:'', Avg_Quality:'', Real_Time_Quality:'',NIR_Reading:''}]
  loginUserData = [{id:'',Username:'',Password:''}]

  constructor(private api: ApiService){
    this.getTanks();
  }
  getTanks = ()=>{
    this.api.getAllTanks().subscribe(
      data => {
        this.tanks = data;
      },
      error => {
          console.log(error)
      }
    )
  }
  createlogin = ()=>{
    this.api.createlogin(this.loginUserData).subscribe(
      data => {
        this.loginUserData.push(data);
      },
      error =>{
        console.log(error);
      }
      
      
    )
  }
  ngOnInit(){
  }
  login(){

    //this.Auth.getUserDetails(usename,password) 
    console.log(this.loginUserData)}
}
