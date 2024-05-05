from alumno.domain.entities.alumno import Student
from alumno.infrastructure.repositories.alumno_repository import MongoDBStudentRepository
from datetime import datetime

class RegisterStudent:
    def __init__(self, student_repository: MongoDBStudentRepository):
        self.student_repository = student_repository

    def execute(self, name, career, initial_status):
        existing_student = self.student_repository.find_by_name(name)
        if existing_student:
            raise ValueError("Ya existe un alumno con ese nombre")
        
        existing_student = self.student_repository.find_by_enrollment(enrollment)
        if existing_student:
            raise ValueError("Ya existe un alumno con esa matrícula")
        year = datetime.now().strftime("%y")
        status_code = "1" if initial_status == "preu" else "3"
        
        last_enrollment_number = self.student_repository.get_last_enrollment_number(year, status_code)
        next_enrollment_number = str(int(last_enrollment_number[-3:]) + 1).zfill(3)

        enrollment = year + status_code + next_enrollment_number

        student = Student(name, career, enrollment, initial_status)
        self.student_repository.save(student)
