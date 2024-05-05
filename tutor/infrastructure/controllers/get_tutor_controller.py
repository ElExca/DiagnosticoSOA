from flask import Blueprint, jsonify
from tutor.application.usecases.get_tutors import GetTutors
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

get_tutor_blueprint = Blueprint('get_tutor', __name__)

def initialize_endpoints(repository):
    get_tutors_usecase = GetTutors(tutor_repository=repository)

    @get_tutor_blueprint.route('/', methods=['GET'])
    def list_tutors():
        tutors = get_tutors_usecase.execute()
        if tutors:
            tutor_list = []
            for tutor in tutors:
                tutor_list.append({
                    'nombre': tutor.first_name,
                    'primer apellido': tutor.last_name,
                    'segundo apellido': tutor.second_last_name,
                    'tutor_id': tutor.tutor_id
                })
            return jsonify({"tutores": tutor_list}), 200
        else:
            return jsonify({"message": "No se encontraron tutores"}), 404
