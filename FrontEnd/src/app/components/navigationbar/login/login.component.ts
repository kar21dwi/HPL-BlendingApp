import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username;
  password;
  check;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }

  getcredentialscheck = () => {
    this.api.GetCredentialsCheck(this.username , this.password).subscribe(
     data => {
       this.check = data;
       console.table(this.check);
     },
     error => {
         console.log(error)
     }     
    )
  
   }

}
