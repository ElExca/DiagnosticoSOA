class Tutor:
    def __init__(self, first_name, last_name, second_last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.second_last_name = second_last_name
        self.tutor_id = self.generate_tutor_id()
        self.alumnos = []

    def generate_tutor_id(self):
        return self.first_name[0].upper() + self.last_name.capitalize()
    
    def add_alumno(self, alumno):
        self.alumnos.append(alumno)