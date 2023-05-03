import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterComponent } from './register/register.component';
import { CarritoComponent } from './carrito/carrito.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { HomeComponent } from './home/home.component';
import { PerfilComponent } from './perfil/perfil.component';

const routes: Routes = [
  {path: '', redirectTo:"/home", pathMatch: "full"},
  {path:'home', component: HomeComponent},
  {path: 'perfil', component: PerfilComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'cart', component: CarritoComponent},
  {path: '**', component: PageNotFoundComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
