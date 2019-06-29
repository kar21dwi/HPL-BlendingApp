import {
	Directive,
	ElementRef,
	Renderer2,
	HostListener,
	NgModule,
	Input,
	Output,
	EventEmitter,
	OnInit,
	HostBinding,
	AfterContentChecked,
	Inject
} from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { ApiService } from 'src/app/api.service';
import Swal from 'sweetalert2';
declare var jquery: any;
declare var $: any;

export enum KEY_CODE {
	TAB = 9
}

/* ********ripple effect directive**************** */
@Directive({
	selector: '[appRippleeffect]'
})
export class RippleeffectDirective {
	constructor(private el: ElementRef, private api: ApiService, private renderer: Renderer2) {}

	@HostListener('click', [ '$event' ])
	clickripple(event: MouseEvent) {
		console.log(this.el);
		const parent = this.el.nativeElement;
		const circle = document.createElement('div');
		parent.appendChild(circle);

		const d = parent.clientWidth / 2;
		circle.style.width = circle.style.height = d + 'px';
		circle.style.left = event.clientX - parent.offsetLeft - d / 2 + 'px';
		circle.style.top = event.clientY - parent.offsetTop - d / 2 + 'px';

		circle.classList.add('ripple');
	}
}

/* ******************************** */

/* ********first page tanks dropwodn directive**************** */
@Directive({
	selector: '[appTankdropdown]'
})
export class TankdropdownrDirective implements AfterContentChecked {
	@Input() rowno: number = -1;
	@Input() currentrow: number = -1;
	@HostBinding('style.backgroundColor') background: string;

	constructor(private el: ElementRef, private api: ApiService, private renderer: Renderer2) {}
	ngAfterContentChecked() {
		/*
		if (this.rowno == 1) {
			console.log('inside directive');
			this.background = 'red';
		} else {
			this.background = 'blue';
		}
		*/
		if (this.rowno == this.currentrow) {
			this.background = '#ececec';
		} else {
			this.background = 'transparent';
		}
	}
}

/* ******************************** */

/* ********list highlighter directive**************** */

@Directive({
	selector: '[appListhighlighter]'
})
export class ListhighlighterDirective implements AfterContentChecked {
	@Input() rowno: number = -1;
	@Input() currentrow: number = -1;
	@HostBinding('style.backgroundColor') background: string;

	constructor(private el: ElementRef, private api: ApiService, private renderer: Renderer2) {}
	ngAfterContentChecked() {
		/*
		if (this.rowno == 1) {
			console.log('inside directive');
			this.background = 'red';
		} else {
			this.background = 'blue';
		}
		*/
		if (this.rowno == this.currentrow) {
			this.background = '#ececec';
		} else {
			this.background = 'transparent';
		}
	}
}

/* ******************************** */

@Directive({
	selector: '[appTabpress]'
})
export class TabpressDirective implements AfterContentChecked {
	@Input() highlight: boolean = true;
	@HostBinding('style.backgroundColor') background: string;

	constructor(private el: ElementRef, private api: ApiService, private renderer: Renderer2) {}
	ngAfterContentChecked() {
		if (this.highlight) {
			console.log('inside directive');
			this.background = 'red';
		} else {
			this.background = 'blue';
		}
	}

	/*

	@HostListener('click')
	abc() {
		console.log('clicked');
		this.renderer.setStyle(this.el.nativeElement, 'top', '-152px');
		this.renderer.setStyle(this.el.nativeElement, 'width', '70px');
		this.renderer.setStyle(this.el.nativeElement, 'height', '70px');
	}

	@HostListener('mouseenter')
	ab() {
		console.log('inside');
		this.renderer.setStyle(this.el.nativeElement, 'position', 'relative');
		this.renderer.setStyle(this.el.nativeElement, 'top', '0px');
		this.renderer.setStyle(this.el.nativeElement, 'width', '150px');
		this.renderer.setStyle(this.el.nativeElement, 'height', '153px');
		this.renderer.setStyle(this.el.nativeElement, 'transition', 'all 0.5s ease-out');
	}*/

	@HostListener('keyup', [ '$event' ])
	keyEvent1(event: KeyboardEvent) {
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
	constructor(el: ElementRef, private api: ApiService) {}

	@HostListener('keyup', [ '$event' ])
	keyEvent2(e: KeyboardEvent) {
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
			mins = parseInt($('#tank' + i + 'amt').val(), 10) || 0;
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
								add = parseInt($('#tank' + j + 'amt').val(), 10) || 0;

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

						Swal.fire({
							title: 'Naphtha Stock Transfered',
							text: 'Maximum transfer limit for the tank: ' + (totalstock - filled),
							type: 'warning'
						});
						check = false;
					}
				}
			}
		}
	}
}

// tslint:disable-next-line: max-classes-per-file
@Directive({
	selector: '[appMouse]'
})
export class MouseDirective {
	constructor(el: ElementRef, private api: ApiService) {}

	@HostListener('mousedown', [ '$event' ])
	mouseEvent(e: MouseEvent) {
		for (let j = 1; j < 6; j++) {
			if ($('#tank' + j + 'amt').val() == '') {
				$('#tank' + j + 'amt').val(0);
			}
		}
	}
}
