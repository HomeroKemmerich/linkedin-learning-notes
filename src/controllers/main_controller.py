from views.main_view import MainView
from constants import SEPARATORS

class MainController:
    raw_content: str
    language: str
    destination: str

    def __init__(self, language='en_us'):
        self.input_file = None
        self.output_file = None
        self.raw_content = None
        self.language = language

    #region Methods
    def start(self):
        self.view = MainView(self)
        self.view.open()

    def process_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            self.raw_content = file.read()
        
        raw_chapters = self.raw_content.split(SEPARATORS['CHAPTER'])

        course_metadata = raw_chapters.pop(0).split('\n\n')
        # course_title = course_metadata[0].replace(texts[], '')
    #endregion

    #region Getters and Setters
    def get_input_file(self):
        return self.input_file

    def set_input_file(self, input_file):
        self.input_file = input_file

    def get_output_file(self):
        return self.output_file

    def set_output_file(self, output_file):
        self.output_file = output_file

    def get_raw_content(self):
        return self.raw_content
    
    def set_raw_content(self, raw_content):
        self.raw_content = raw_content
    
    def get_language(self):
        return self.language
    
    def set_language(self, language):
        self.language = language

    def get_destination(self):
        return self.destination
    
    def set_destination(self, destination):
        self.destination = destination

    #endregion