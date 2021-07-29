# Attendance-Website-Using-Facial-Recognition-Django

## Technologies Used
[<img  alt="Django" width="80px" height="30px" height="30px" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />][DJANGO]
[<img  alt="JavaScript" width="80px" height="30px" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />][JAVASCRIPT]
[<img  alt="Python" width="80px" height="30px" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen">][PYTHON]
[<img  alt="SQL" width="80px" height="30px" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />][SQL]
[<img  alt="html5" width="80px" height="30px" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />][HTML]
[<img  alt="CSS3" width="80px" height="30px" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />][CSS]


## Video
![gif](Video/facial-recog.gif)

## Description

The attendance management system proposes login for both students and faculty. Student has to register first using his personal information such as name, contact details, Admission number(unique)branch and semester in which he/she is attending lectures . The unique ID(Admission number) which is recorded by students is used by the faculty for identification. The student's facial features are then recorded in the database with the help of a camera . These recorded facial features are then used for allowing students to easily login without any extra credentials . The model will be created using OpenCV. It detects the faces in the image and compares it with the recognized faces in the database.Facial recognition technique for automated attendance management system is implemented by using deep learning. It helps in conversion of the frames of the video into images so that the face of the student can be easily recognized for their attendance so that the attendance database can be easily reflected automatically . This model will be a successful technique to manage the attendance and records of students as faculty will get the names and information of students present in an Microsoft excel sheet too which can be further uploaded directly by faculty wherever necessary.

## Getting Started

### System Architecture
![plot](Video/System_Architecture.png)



### Dependencies

* All dependencies can be found in requirements.txt

### Installing

* Clone the project install all the dependencies.


### Functionalities 

 * Student enrolment
 * Image pre-processing and noise removal
 * Model training
 * Face Detection
 * Database Creation For Attendance
 * Final Report Generation

### Executing program

* Just use the django commands to run the website 
* ex.python manage.py runserver

[JAVASCRIPT]: https://devdocs.io/javascript/
[DJANGO]: https://docs.djangoproject.com/en/3.1/
[PYTHON]: https://www.python.org/doc/
[SQL]: https://dev.mysql.com/doc/
[HTML]: https://devdocs.io/html/
[CSS]: https://developer.mozilla.org/en-US/docs/Web/CSS
