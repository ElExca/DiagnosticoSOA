from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

class GetAlumnosByTutor:
    def __init__(self, tutor_repository: MongoDBTutorRepository):
        self.tutor_repository = tutor_repository

    def execute(self, tutor_id):
        tutor = self.tutor_repository.find_by_id(tutor_id)
        if tutor:
            return tutor.alumnos
        else:
            return []
