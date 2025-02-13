from constants import SEPARATORS, LINKEDIN_LEARNING_URL
from functions import unformat, timestamp_to_seconds
from views.main_view import MainView
from constants.language import texts
from models import (
    Course,
    Chapter,
    Video,
    Note
)


class MainController:
    raw_content: str
    language: str
    destination: str

    def __init__(self, language='en_us'):
        self.input_file = None
        self.output_file = None
        self.raw_content = None
        self.parsed_content = None
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
        course_title = course_metadata[0].replace(texts[self.language]['course_name'], '')
        course_description = course_metadata[1].replace(texts[self.language]['course_description'], '')
        course_stub = unformat(course_title.lower().replace(':', '').replace(' ', '-'))

        chapter_list = []
        for i in range(0, len(raw_chapters), 2):
            chapter_title = raw_chapters[i].replace('\n', '').replace(texts[self.language]['chapter'], '')

            raw_videos = raw_chapters[i + 1].split(SEPARATORS['VIDEO'])
            raw_videos = [video for video in raw_videos if video != SEPARATORS['SECTION']]

            chapter_videos = []
            for j in range(0, len(raw_videos), 2):
                video_title = raw_videos[j].replace('\n', '').replace(texts[self.language]['video'], '')
                video_stub = unformat(video_title.lower().replace(' ', '-')).replace('?', '')

                raw_notes = raw_videos[j + 1].split(SEPARATORS['TIMESTAMP'])[1:]
                video_notes = []
                for k in range(len(raw_notes)):
                    split_note = raw_notes[k].split(SEPARATORS['INLINE_SPACING'])

                    timestamp = f'00{split_note[0]}'
                    text = split_note[1].replace(SEPARATORS['SECTION'], '').replace(SEPARATORS['NEW_LINE_SPACING'], '')
                    url = f'{LINKEDIN_LEARNING_URL}/{course_stub}/{video_stub}?seekTo={timestamp_to_seconds(timestamp)}'

                    video_notes.append(Note(timestamp, url, text))

                chapter_videos.append(Video(video_title, video_notes))

            chapter_list.append(Chapter(chapter_title, chapter_videos))
        
        self.parsed_content = Course(course_title, course_description, chapter_list)
    
    def export_file(self):
        if self.destination == 'File':
            if 'json' in self.output_file:
                with open(self.output_file, 'w', encoding='utf-8') as file:
                    file.write(self.parsed_content.to_json())
            elif 'md' in self.output_file:
                with open(self.output_file, 'w', encoding='utf-8') as file:
                    file.write(self.parsed_content.to_md())
        elif self.destination == 'Readwise':
            pass
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