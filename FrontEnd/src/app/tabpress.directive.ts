import { Directive, ElementRef, HostListener, NgModule, Input, Output, EventEmitter } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import Swal from 'sweetalert2';
declare var jquery: any;
declare var $: any;

export enum KEY_CODE {
  TAB = 9,
}

@Directive({
  selector: '[appTabpress]',
})
export class TabpressDirective {


  constructor(el: ElementRef, private api: ApiService) { 
    
  }


  @HostListener('keyup', ['$event']) keyEvent1(event: KeyboardEvent) {

    if (event.keyCode === KEY_CODE.TAB) {

        console.log('pressed tab');
        this.api.sendTabPressStatus(true);

    }
      
  }
  }





@Directive({
  selector: '[appTab]'
})

export class TabDirective {

  constructor(el: ElementRef, private api: ApiService) {

  }

  @HostListener('keyup', ['$event']) keyEvent2(e: KeyboardEvent) {


    $('#tank1amt').click();


    let keyCode = e.keyCode || e.which;

    if (keyCode == 9) {
        for (let j = 1; j < 6; j++) {
            if ($('#tank' + j + 'amt').val() == '') {
            $('#tank' + j + 'amt').val(0);
          }
        }

      }




    let sum = 0;
    let mins;

    for (let i = 1; i < 6; i++) {
      mins = parseInt($('#tank' + i + 'amt').val() , 10) || 0;
      sum = sum + mins;
    }

    const id = $(e.currentTarget).attr('id');
    
    const totalstock = $('#totalstock').val();

    if (sum > totalstock) {
      let check = true;
      for (let i = 1; i < 6; i++) {
        if (check) {

          if (id == 'tank' + i + 'amt') {

            let filled = 0;
            let add: number;

            for (let j = 1; j < 6; j++) {
              if (j != i) {

                add = parseInt($('#tank' + j + 'amt').val() , 10) || 0;

                filled = filled + add;
                if (add == 0) {
                  $('#tank' + j + 'amt').prop('disabled', true);
                } else {
                  $('#tank' + j + 'first').prop('disabled', false);
                }
              } else {
                $('#tank' + j + 'first').prop('disabled', false);
              }

            }

            $(e.currentTarget).val(totalstock - filled);

            Swal.fire({title: 'Naphtha Stock Transfered',
            text: 'Maximum transfer limit for the tank: ' + (totalstock - filled),
            type: 'warning'});
            check = false;


        }
        }

      }
    }

  }

  }

@Directive({
    selector: '[appMouse]'
  })

  export class MouseDirective {

    constructor(el: ElementRef, private api: ApiService) { }

    @HostListener('mousedown', ['$event']) mouseEvent(e: MouseEvent) {

     for (let j = 1; j < 6; j++) {
          if ($('#tank' + j + 'amt').val() == '') {
          $('#tank' + j + 'amt').val(0);
        }
     }

  }

  }



