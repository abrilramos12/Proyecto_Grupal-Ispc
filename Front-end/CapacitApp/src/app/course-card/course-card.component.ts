import { Component, Input, OnInit } from '@angular/core';
import { Course } from '../Models/Course';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.css']
})


export class CourseCardComponent implements OnInit{

  @Input() course!: Course;

  imagePath!: string;

  constructor(){  

  }
  
  ngOnInit(): void {
    this.imagePath = this.course.imagePath;
  }

}
