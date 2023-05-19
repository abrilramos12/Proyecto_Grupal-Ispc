import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Route } from '@angular/router';



@Injectable({
  providedIn: 'root'
})
export class RouteService {
    private url:string="http://localhost:3000"

  constructor(private htttp: HttpClient) { }
//creo metodo get

getRoutes(): Observable<Route[]> //retorna un observable que es un array de rutas

}
