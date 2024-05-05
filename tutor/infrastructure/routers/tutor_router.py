from flask import Blueprint
from tutor.infrastructure.controllers.create_tutor_controller import create_tutor_blueprint, initialize_endpoints as create_tutor_endpoints
from tutor.infrastructure.controllers.get_tutor_controller import get_tutor_blueprint, initialize_endpoints as get_tutor_endpoints
from tutor.infrastructure.controllers.assign_alumnos_to_tutor_controller import assign_alumnos_to_tutor_blueprint, initialize_endpoints as assign_alumnos_to_tutor_endpoints
from tutor.infrastructure.controllers.get_alumnos_by_tutor_controller import get_alumnos_by_tutor_blueprint, initialize_endpoints as get_alumnos_by_tutor_endpoints
from tutor.infrastructure.repositories.tutor_repository import MongoDBTutorRepository

tutor_router = Blueprint('tutor_router', __name__)

def initialize_endpoints(repository):
    create_tutor_endpoints(repository)
    get_tutor_endpoints(repository)
    get_alumnos_by_tutor_endpoints(repository)
    assign_alumnos_to_tutor_endpoints(repository)


initialize_endpoints(MongoDBTutorRepository(connection_string='mongodb://localhost:27017/', database_name='APIdiagnostico'))

tutor_router.register_blueprint(create_tutor_blueprint, url_prefix='/api/tutores')
tutor_router.register_blueprint(get_tutor_blueprint, url_prefix='/api/tutores')
tutor_router.register_blueprint(assign_alumnos_to_tutor_blueprint, url_prefix='/api/tutores')
tutor_router.register_blueprint(get_alumnos_by_tutor_blueprint, url_prefix='/api/tutores')