import { Component, OnInit, Input, AfterContentChecked } from '@angular/core';
import { ApiService } from 'src/app/api.service';
@Component({
  selector: 'app-modelnirblendquality',
  templateUrl: './modelnirblendquality.component.html',
  styleUrls: ['./modelnirblendquality.component.css']
})
export class ModelnirblendqualityComponent implements OnInit, AfterContentChecked {
  nirmodel = 0;
  check = true;
  @Input() nextclicked : boolean;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  ngAfterContentChecked(){
    this.getnirmodel();

    }
  getnirmodel = () => {
    if(this.nextclicked == true && this.check){
      this.check =false;
    this.api.GetNirModel().subscribe(
      data => {
        this.nirmodel = data;
        console.table(this.nirmodel)
      },
      error => {
          console.log(error)
      }
    )

  }

}
}