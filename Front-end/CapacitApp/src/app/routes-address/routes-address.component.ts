import { Component, Input } from '@angular/core';
import { Route } from '@angular/router';

@Component({
  selector: 'app-routes-address',
  templateUrl: './routes-address.component.html',
  styleUrls: ['./routes-address.component.css']
})
export class RoutesAddressComponent {

  @Input() route!: Route;

  imagePath!: string ;

  constructor(){

  }
  ngOnInit():void{
    this.imagePath = this.route.imagePath;
  }
}
