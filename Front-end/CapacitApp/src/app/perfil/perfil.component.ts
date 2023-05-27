import { Component, Input } from '@angular/core';
import { PerfilService } from '../services/perfil.service';
import { Perfil } from '../Models/Perfil';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css'],

})


export class PerfilComponent{

  @Input() perfil: any;

  constructor(private perfilService: PerfilService) { }


  ngOnInit() {
    const usuarioId = 2;
    this.getPerfil(usuarioId);
  }

  getPerfil(usuarioId: number) {
    this.perfilService.getPerfil(usuarioId).subscribe({
      next: (perfil) => {
        this.perfil = perfil;
        console.log('Perfil del usuario:', this.perfil);
      },
      error: (error) => {
        console.error('Error al obtener el perfil:', error);
      }
    });
  }


}
