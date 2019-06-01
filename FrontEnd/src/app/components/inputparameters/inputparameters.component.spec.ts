import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InputparametersComponent } from './inputparameters.component';

describe('InputparametersComponent', () => {
  let component: InputparametersComponent;
  let fixture: ComponentFixture<InputparametersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InputparametersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InputparametersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
