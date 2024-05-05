from flask import Blueprint, request, jsonify
from tutor.application.usecases.assign_alumnos_to_tutor import AssignAlumnosToTutor
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

assign_alumnos_to_tutor_blueprint = Blueprint('assign_alumnos_to_tutor', __name__)

def initialize_endpoints(repository):
    assign_alumnos_to_tutor_usecase = AssignAlumnosToTutor(tutor_repository=repository)
    
    @assign_alumnos_to_tutor_blueprint.route('/<tutor_id>/alumnos', methods=['POST'])
    def assign_alumnos_to_tutor(tutor_id):
        data = request.get_json()

        if not data or not 'tutorados' in data:
            return jsonify({"error": "Se requiere una lista de alumnos tutorados"}), 400

        tutorados = data.get('tutorados')

        try:
            assign_alumnos_to_tutor_usecase.execute(tutor_id, tutorados)
            return jsonify({"message": "Alumnos asignados al tutor exitosamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
