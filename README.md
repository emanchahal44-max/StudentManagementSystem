Student Management System
A simple Python program to manage students, subjects, enrollments, grades, and attendance.

How to Run 
Clone the repository:
   git clone https://github.com/emanchahal44-max/StudentManagementSystem.git
   
   cd StudentManagementSystem/student_management_system
   
or through python main.py

when the programm runs, this menu will appear
      Add Student
      Add Subject
      Enroll Student
      Add Grade
      Mark Attendance (subject-wise Present or absent)
      View Student Report
      View All Students
      View Enrollments
      Exit
      
When marking attendance, the system will ask each student in the chosen subject whether they are Present (P) or Absent (A). Attendance percentages are calculated automatically!

Follow the menu to manage students, subjects, enrollments, grades, attendance, and view reports.

Features
Add students (ID, name, section)
Add subjects (code, name, credit hours)
Enroll students in subjects
Record grades per student per subject
Mark attendance (Present/Absent) and calculate attendance %
View student reports (grades and attendance)
View all students and enrollments

Data Storage
Data is stored in text files inside the data/ folder:
          students.txt → Student information
          subjects.txt → Subject information
          enrollments.txt → Student-subject enrollments
          records.txt → Grades and attendance per student per subject

Classes Used
Student → Handles student details
Subject → Handles subject details
Record → Handles grades and attendance
SystemManager → Manages all operations like adding, enrolling, grading, attendance, and reports


