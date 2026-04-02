CREATE DATABASE School_DATABASE;
use School_DATABASE;


CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    grade VARCHAR(10),
    created_at TIMESTAMP
);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE enrollments (
    id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrolled_at TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);



INSERT INTO students VALUES
(1,'Rahul','A','2024-01-10'),
(2,'Priya','B','2024-01-11'),
(3,'Amit','A','2024-01-12'),
(4,'Neha','C','2024-01-13'),
(5,'Ravi','B','2024-01-14'),
(6,'Anita','A','2024-01-15'),
(7,'Vikas','C','2024-01-16'),
(8,'Pooja','B','2024-01-17'),
(9,'Arjun','A','2024-01-18'),
(10,'Kiran','B','2024-01-19');



INSERT INTO courses VALUES
(1,'Mathematics','Science'),
(2,'Physics','Science'),
(3,'History','Arts'),
(4,'Computer Science','Technology'),
(5,'English','Language')
(6,'Python','Technology');



INSERT INTO enrollments VALUES
(1,1,1,'2024-02-01'),
(2,1,2,'2024-02-02'),
(3,2,3,'2024-02-02'),
(4,2,4,'2024-02-03'),
(5,3,1,'2024-02-04'),
(6,3,5,'2024-02-05'),
(7,4,2,'2024-02-05'),
(8,4,3,'2024-02-06'),
(9,5,4,'2024-02-06'),
(10,5,5,'2024-02-07'),
(11,6,1,'2024-02-07'),
(12,6,3,'2024-02-08'),
(13,7,2,'2024-02-08'),
(14,7,4,'2024-02-09'),
(15,8,5,'2024-02-09'),
(16,8,1,'2024-02-10'),
(17,9,2,'2024-02-10'),
(18,9,3,'2024-02-11'),
(19,10,4,'2024-02-11'),
(20,10,5,'2024-02-12'),
(21,10,6,'2024-02-12'),
(22,10,5,'2024-02-12'),
(23,8,6,'2024-02-01');



SELECT COUNT(*)
FROM enrollments e
JOIN courses c
ON e.course_id = c.id
WHERE c.name = 'Python'
AND YEAR(e.enrolled_at) = 2024;


SELECT COUNT(*)
FROM enrollments e
JOIN courses c
ON e.course_id = c.id
WHERE c.name = 'English';



SELECT * FROM courses;