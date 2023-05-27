import { Component } from '@angular/core';
import { CourseService } from '../services/course.service'
import { Course } from '../Models/Course';


@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.css']
})
export class CursosComponent {
  courses: Course[] = [];
  newCourse: Course = {} as Course;

  constructor(private service: CourseService) {

    this.getAllCourses()
  }

  getAllCourses() {
    this.service.getCourses().subscribe({
      next: (data) => {
        this.courses = data;
      },
      error: (error) => {
        console.log("No se pueden traer los usuarios", error)
      }
    });
  }

  createCourse() {
    this.service.createCourse(this.newCourse)
      .subscribe({
        next: (data) => {
          console.log("Curso creado exitosamente", data)
          this.newCourse = {} as Course;

        },
        error: (error) => {
          console.log("Error al creal el curso", error)
        }
      })
  }

}
