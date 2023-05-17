import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Course } from "../Models/Course"
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  url:string = 'http://localhost:3000/'

  constructor(private http: HttpClient) { }

  obtenerCursos(): Observable<Course[]> {
    return this.http.get<Course []>(this.url + "courses")
  }
}
