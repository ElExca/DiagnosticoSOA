from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

class GetTutors:
    def __init__(self, tutor_repository: MongoDBTutorRepository):
        self.tutor_repository = tutor_repository

    def execute(self):
        return self.tutor_repository.find_all()
