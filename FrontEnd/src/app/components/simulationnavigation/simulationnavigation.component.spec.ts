import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationnavigationComponent } from './simulationnavigation.component';

describe('SimulationnavigationComponent', () => {
  let component: SimulationnavigationComponent;
  let fixture: ComponentFixture<SimulationnavigationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SimulationnavigationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SimulationnavigationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
