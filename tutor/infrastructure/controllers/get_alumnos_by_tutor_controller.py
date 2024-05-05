from flask import Blueprint, jsonify
from tutor.application.usecases.get_alumnos_by_tutor import GetAlumnosByTutor
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

get_alumnos_by_tutor_blueprint = Blueprint('get_alumnos_by_tutor', __name__)

def initialize_endpoints(repository):
    get_alumnos_by_tutor_usecase = GetAlumnosByTutor(tutor_repository=repository)

    @get_alumnos_by_tutor_blueprint.route('/<tutor_id>/alumnos', methods=['GET'])
    def get_alumnos_by_tutor(tutor_id):
        alumnos = get_alumnos_by_tutor_usecase.execute(tutor_id)
        if alumnos:
            return jsonify({"alumnos": alumnos}), 200
        else:
            return jsonify({"message": "No se encontraron alumnos para este tutor"}), 404
        
    
