import { Component, Input } from '@angular/core';
import{ Route} from '../models/routes'

@Component({
  selector: 'app-routes-address',
  templateUrl: './routes-address.component.html',
  styleUrls: ['./routes-address.component.css']
})
export class RoutesAddressComponent {

  @Input() ruta!: Route;

  imagePath!: string ;

  constructor(){

  }


}
