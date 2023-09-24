# Assignment 2

Records students, courses, major they enroll in.

**Conceptual Diagram**

![Conceptual](https://github.com/ptphamtx/assignment2/assets/113536208/9c2f4a5c-8f68-47a1-b0d6-a5d5177ce9f1)

* Student and Course has a many to many relationship through Course Enrollment, where a student can take many courses and a course can be taken by many students.
* Each student can select a major to pursue. A major can be selected by many students. This is a many-to-one relationship
* A major is administered by one faculty (College Of). Under one College Of, there can be many majors.
* Also, one College Of can oversee many courses while a course can be associated with jut one College Of. 
-----

**Logical Diagram**

![Logical](https://github.com/ptphamtx/assignment2/assets/113536208/4566cd40-74ea-4c7e-af19-365a1988bdc0)

There are 5 tables:
* The Student table stores information about student ID, first name, last name, DOB and their major. 
* Course Enrollment is an intermediate table formed by a many-to-many relationship between Student and Course.
* In the Course Enrollment table, it shows the student ID, course ID, semester and year about each course a student's enrolled in.
* The Course table holds attributes of about each course like its number, name, id and credit hours.
* Major information is stored in the Major table, whereas as Faculty table stores information about their College Of.
-----

**Physical Diagram**

![Physical](https://github.com/ptphamtx/assignment2/assets/113536208/71621432-5974-4734-b631-d1ab1f91012a)

* The Student table connects with the Major table through a foreign key (major_id).
* The Major table connects with the Faculty table through a foreign key (faculty_id). 
* The Course table also connects with the Faculty table through a foreign key (faculty_id).
* The Course Enrollment table connects with Student table and Course table through 2 foreign keys it holds. 
