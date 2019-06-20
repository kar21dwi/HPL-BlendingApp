import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TanksdetailComponent } from './tanksdetail.component';

describe('TanksdetailComponent', () => {
  let component: TanksdetailComponent;
  let fixture: ComponentFixture<TanksdetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TanksdetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TanksdetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
