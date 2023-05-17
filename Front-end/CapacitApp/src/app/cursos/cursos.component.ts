import { Component } from '@angular/core';
import {CourseService} from '../services/course.service'
import { Course } from '../Models/Course';

@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.css']
})
export class CursosComponent {
  courses: Course[] = [];

  constructor(private service: CourseService){

    this.service.obtenerCursos().subscribe(data => {
      this.courses = data;
    });

  }


}
