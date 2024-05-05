from flask import Blueprint, request, jsonify
from tutor.application.usecases.register_tutor import RegisterTutor
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository
from tutor.domain.validations.tutor_validations import validate_name, validate_last_name, validate_second_last_name

create_tutor_blueprint = Blueprint('create_tutor', __name__)

def initialize_endpoints(repository):
    register_tutor_usecase = RegisterTutor(tutor_repository=repository)
    
    @create_tutor_blueprint.route('', methods=['POST'])
    def register_tutor():
        data = request.get_json()

        if not data or not all(key in data for key in ['first_name', 'last_name']):
            return jsonify({"error": "Se requieren nombre y apellido"}), 400

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        second_last_name = data.get('second_last_name')

        try:
            register_tutor_usecase.execute(first_name, last_name, second_last_name)
            return jsonify({"message": "Tutor registrado exitosamente"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
