import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RoutesAddressComponent } from './routes-address.component';

describe('RoutesAddressComponent', () => {
  let component: RoutesAddressComponent;
  let fixture: ComponentFixture<RoutesAddressComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RoutesAddressComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RoutesAddressComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
