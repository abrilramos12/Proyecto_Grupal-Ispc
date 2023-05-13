import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  url:string = "http://localhost:3000/"

  constructor(private http: HttpClient) { }

  obtenerCursos() {
    return this.http.get<Object []>(this.url + "courses")
  }
}
