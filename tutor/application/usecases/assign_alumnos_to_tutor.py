from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

class AssignAlumnosToTutor:
    def __init__(self, tutor_repository: MongoDBTutorRepository):
        self.tutor_repository = tutor_repository

    def execute(self, tutor_id, alumno_ids):
        tutor = self.tutor_repository.find_by_id(tutor_id)
        if not tutor:
            raise ValueError("Tutor no encontrado")

        self.tutor_repository.assign_alumnos(tutor, alumno_ids)
