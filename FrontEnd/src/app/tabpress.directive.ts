import { Directive, ElementRef, HostListener } from '@angular/core';
import { ApiService } from 'src/app/api.service';

export enum KEY_CODE {
  TAB = 9,
}

@Directive({
  selector: '[appTabpress]'
})
export class TabpressDirective {

  constructor(el: ElementRef, private api: ApiService) { }


  @HostListener('keyup', ['$event']) keyEvent(event: KeyboardEvent) {
        
    if (event.keyCode === KEY_CODE.TAB) {
      
        console.log('pressed tab')
        this.api.sendTabPressStatus(true);
      
    }
  }

}
