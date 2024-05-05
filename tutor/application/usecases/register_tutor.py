from tutor.domain.entities.tutor import Tutor
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository
from tutor.domain.validations.tutor_validations import validate_name, validate_last_name, validate_second_last_name

class RegisterTutor:
    def __init__(self, tutor_repository: MongoDBTutorRepository):
        self.tutor_repository = tutor_repository

    def execute(self, first_name, last_name, second_last_name=None):
        if not validate_name(first_name):
            raise ValueError("Invalid first name format")

        if not validate_last_name(last_name):
            raise ValueError("Invalid last name format")

        if second_last_name and not validate_second_last_name(second_last_name):
            raise ValueError("Invalid second last name format")

        tutor = Tutor(first_name, last_name, second_last_name)
        self.tutor_repository.save(tutor)
