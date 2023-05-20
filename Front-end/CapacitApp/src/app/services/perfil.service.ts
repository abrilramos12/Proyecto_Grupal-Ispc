import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Perfil } from '../Models/Perfil';

@Injectable({
  providedIn: 'root'
})


export class PerfilService {

  private url = 'http://localhost:3000/perfiles';


  constructor(private http: HttpClient) { }

  getPerfil(usuarioId: number): Observable<Perfil> {
    const url = `${this.url}/${usuarioId}`;
    return this.http.get<Perfil>(url);
  }
}
