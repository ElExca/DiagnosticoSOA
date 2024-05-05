from pymongo import MongoClient
from tutor.domain.entities.tutor import Tutor
from alumno.domain.entities.alumno import Student

class MongoDBTutorRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db['tutores']

    def save(self, tutor: Tutor):
        tutor_data = {
            'first_name': tutor.first_name,
            'last_name': tutor.last_name,
            'second_last_name': tutor.second_last_name,
            'tutor_id': tutor.tutor_id
        }
        result = self.collection.insert_one(tutor_data)
        #tutor.tutor_id = str(result.inserted_id)

    def find_by_id(self, tutor_id):
        tutor_data = self.collection.find_one({'tutor_id': tutor_id})
        if tutor_data:
            return Tutor(tutor_data['first_name'], tutor_data['last_name'], tutor_data.get('second_last_name'))
        return None
    
    def find_all(self):
        tutor_data = self.collection.find({})
        tutors = []
        for tutor in tutor_data:
            tutors.append(Tutor(tutor['first_name'], tutor['last_name'], tutor.get('second_last_name')))
        return tutors
    
    def assign_alumnos(self, tutor, alumno_ids):
        for alumno_id in alumno_ids:
            alumno = self.db['alumnos'].find_one({'enrollment': alumno_id})
            if not alumno:
                raise ValueError(f"El alumno con matricula {alumno_id} no existe.")

        self.collection.update_one(
            {'tutor_id': tutor.tutor_id},
            {'$addToSet': {'alumnos': {'$each': alumno_ids}}},
        )

        tutor.alumnos.extend(alumno_ids)


    def get_students_by_tutor_id(self, tutor_id):
        tutor_data = self.collection.find_one({'tutor_id': tutor_id})
        if tutor_data:
            student_ids = tutor_data.get('student_ids', [])
            students_data = self.db['alumnos'].find({'enrollment': {'$in': student_ids}})
            students = []
            for student_data in students_data:
                students.append(Student(
                    name=student_data['name'],
                    career=student_data['career'],
                    enrollment=student_data['enrollment'],
                    initial_status=student_data['initial_status']
                ))
            return students
        else:
            return None