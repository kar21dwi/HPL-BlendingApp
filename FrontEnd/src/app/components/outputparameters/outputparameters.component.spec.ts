import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OutputparametersComponent } from './outputparameters.component';

describe('OutputparametersComponent', () => {
  let component: OutputparametersComponent;
  let fixture: ComponentFixture<OutputparametersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OutputparametersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OutputparametersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
