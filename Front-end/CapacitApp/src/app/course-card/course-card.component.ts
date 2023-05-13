import { Component, Input } from '@angular/core';
import { CourseService } from '../services/course.service'

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.css']
})


export class CourseCardComponent {

  @Input() course!: {
    id: number,
    name: string,
    imagePath: string,
    description: string,
    language: string,
    tag_1: string,
    tag_2: string,
    price: number,
    teacherId: number
  }

  imagePath!: string;

  constructor(private courseService: CourseService){  

  }
  
  ngOnInit(): void {
    this.imagePath = this.course.imagePath;
  }

}
