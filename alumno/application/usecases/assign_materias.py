from alumno.infrastructure.repositories.alumno_repository import MongoDBStudentRepository
from materia.infrastructure.repositories.materia_repository import MongoDBMateriaRepository

class AssignMaterias:
    def __init__(self, student_repository: MongoDBStudentRepository, materia_repository: MongoDBMateriaRepository):
        self.student_repository = student_repository
        self.materia_repository = materia_repository

    def execute(self, enrollment, materias):
        alumno = self.student_repository.find_by_enrollment(enrollment)
        if not alumno:
            raise ValueError("El alumno no existe")

        for materia_nombre in materias:
            materia = self.materia_repository.find_by_name(materia_nombre)
            if not materia:
                raise ValueError(f"La materia '{materia_nombre}' no existe")

        self.student_repository.assign_materias(alumno, materias)
