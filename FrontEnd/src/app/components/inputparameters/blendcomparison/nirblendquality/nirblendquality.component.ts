import { Component, OnInit, Input, AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-nirblendquality',
  templateUrl: './nirblendquality.component.html',
  styleUrls: ['./nirblendquality.component.css']
})
export class NirblendqualityComponent implements OnInit, AfterContentChecked {
  niractual = 0;
  @Input() nextclicked : boolean;
  check = true;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  ngAfterContentChecked(){
    this.getniractual();
  }

  getniractual = () => {
    if(this.nextclicked == true && this.check){
      this.check = false;
    this.api.GetNirActual().subscribe(
      data => {
        this.niractual = data;
        console.table(this.niractual)
      },
      error => {
          console.log(error)
      }
    )

  }

}
}
