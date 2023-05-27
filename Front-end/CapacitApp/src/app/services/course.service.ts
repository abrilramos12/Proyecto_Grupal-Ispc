import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Course } from "../Models/Course"
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  private url:string = 'http://localhost:3000/'

  constructor(private http: HttpClient) { }

  getCourses(): Observable<Course[]> {
    return this.http.get<Course []>(this.url + "courses")
  }

  createCourse(newCourse: Course){
    return this.http.post<Course>(this.url + "courses", newCourse)
  }

  findCourseById(Id: number) {
    
  }

  updateCourse(){}

  deleteCourse(){}
}
