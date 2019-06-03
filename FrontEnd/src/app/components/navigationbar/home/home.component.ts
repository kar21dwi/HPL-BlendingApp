import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  flag = true;

  constructor() { }

  ngOnInit() {
  }

  mainpage() {
    
    if (this.flag == false)
    {
     this.flag = true;
    }
    else
    {
     this.flag = false; 
    }

  }

}
