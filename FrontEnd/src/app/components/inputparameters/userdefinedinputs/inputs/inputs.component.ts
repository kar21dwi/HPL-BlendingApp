import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-inputs',
  templateUrl: './inputs.component.html',
  styleUrls: ['./inputs.component.css']
})
export class InputsComponent implements OnInit {
  inputparameter = 0;
  @Input() suctiontank : any;
  @Input() blendingtank : any;

  constructor(private api: ApiService) { }

  ngOnInit() {
  }
  getselectedtanks = () => {
    this.api.PostUserDefinedInputs().subscribe(
      data => {
        this.inputparameter = data;
      },
      error => {
          console.log(error)
      }
    )


}
}
