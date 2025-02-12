from course import Course

class Controller:
    input_path: str
    output_path: str
    course: Course

    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def read_file(self):
        with open(self.input_path, 'r') as file:
            return file.read()

    def load_course(self):
        
