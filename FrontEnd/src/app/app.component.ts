import { Component } from '@angular/core';
import { ApiService } from './api.service';

//new line add

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  tanks = [{id:'', Paraffin:'', Olefins:'', Aromatics:'', Napthene:'',INIP_Ratio:'',Density:'',
              Sulfur:'', IBP:'', FBP:'',Paraffin_R:'',Olefins_R:'',Density_R:'',Paraffin_NIR:'',
              Olefins_NIR:'',Density_NIR:'',Level:'',Weight:''}]
  loginUserData = [{id:'',Username:'',Password:''}]

  constructor(private api: ApiService){
  //  this.getTanks();
  }
  /*
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
    console.log(this.loginUserData)
  }

  */
}
