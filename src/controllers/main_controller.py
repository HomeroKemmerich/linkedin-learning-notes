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
    course: Course

    def __init__(self, language='en_us'):
        self.input_file = None
        self.output_file = None
        self.raw_content = None
        self.language = language
        self.view = MainView(self)
        self.course = None


    def start(self):
        self.view.open()

    #region File methods
    def import_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            self.raw_content = file.read()

    def process_file(self):
        self.import_file()

        raw_chapters = self.raw_content.split(SEPARATORS['CHAPTER'])

        [course_title, course_description] = self.get_course_metadata(raw_chapters[0])
        self.course = Course(course_title, course_description)
        self.course.set_chapters(self.get_chapters(raw_chapters[1:]))
    
    def export_file(self):
        if self.destination == 'File':
            if 'json' in self.output_file:
                with open(self.output_file, 'w', encoding='utf-8') as file:
                    file.write(self.course.to_json())
            elif 'md' in self.output_file:
                with open(self.output_file, 'w', encoding='utf-8') as file:
                    file.write(self.course.to_md())
        elif self.destination == 'Readwise':
            pass
    #endregion

    #region Model methods
    def get_course_metadata(self, chapter0):
        course_metadata = chapter0.split('\n\n')
        course_title = course_metadata[0].replace(texts[self.language]['course_name'], '')
        course_description = course_metadata[1].replace(texts[self.language]['course_description'], '')
        return [course_title, course_description]

    def get_notes(self, raw_notes, video_stub):
        notes = []
        for i in range(len(raw_notes)):
            split_note = raw_notes[i].split(SEPARATORS['INLINE_SPACING'])
            timestamp = f'00{split_note[0]}'
            text = split_note[1].replace(SEPARATORS['SECTION'], '').replace(SEPARATORS['NEW_LINE_SPACING'], '')
            url = f'{LINKEDIN_LEARNING_URL}/{self.course.stub}/{video_stub}?seekTo={timestamp_to_seconds(timestamp)}'
            notes.append(Note(timestamp, url, text))
        return notes
        
    def get_videos(self, raw_videos):
        videos = []
        for i in range(0, len(raw_videos), 2):
            video_title = raw_videos[i].replace('\n', '').replace(texts[self.language]['video'], '')

            video = Video(video_title)
            raw_notes = raw_videos[i + 1].split(SEPARATORS['TIMESTAMP'])[1:]
            video.set_notes(self.get_notes(raw_notes, video.stub))

            videos.append(video)
        return videos

    def get_chapters(self, raw_chapters):
        chapters = []
        for i in range(0, len(raw_chapters), 2):
            chapter_title = raw_chapters[i].replace('\n', '').replace(texts[self.language]['chapter'], '')
            chapter = Chapter(chapter_title)

            raw_videos = raw_chapters[i + 1].split(SEPARATORS['VIDEO'])
            raw_videos = [video for video in raw_videos if video != SEPARATORS['SECTION']]

            chapter.set_videos(self.get_videos(raw_videos))

            chapters.append(chapter)
        return chapters
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