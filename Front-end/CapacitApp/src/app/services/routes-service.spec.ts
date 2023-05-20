import { TestBed } from '@angular/core/testing';

import { RouteService } from './routes-service';

describe('RoutesSericeService', () => {
  let service: RouteService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RouteService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
