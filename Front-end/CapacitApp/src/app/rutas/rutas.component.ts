import { Component } from '@angular/core';
import { Route } from '../models/routes';
import { RouteService } from '../services/routes-service'

@Component({
  selector: 'app-rutas',
  templateUrl: './rutas.component.html',
  styleUrls: ['./rutas.component.css']
})
export class RutasComponent {
 routes: Route[] = [];  //donde guardo los array de servicio rutas

 constructor(private services: RouteService){

   this.getAllRoutes()//llamo a esta funcion
 }

getAllRoutes(){ //llama al servicicio y al metodo get
  this.services.getRoutes().subscribe({ // se susbcribe a ese observable
    next: (data) =>{  // para usar el dato
      this.routes = data;
    },

    error: (error) =>{//para menejar errores
      console.log(error.nsg)
    }
  });//aca ya tenemos los datos ...
}}
