from constants import SEPARATORS, LINKEDIN_LEARNING_URL
from functions import unformat, timestamp_to_seconds
from views.main_view import MainView
from constants.language import texts
from models import (
    Course,
    Chapter,
    Video,
    Note,
    Settings
)
from services import FileService


class AppController:
    course: Course
    settings: Settings

    def __init__(self, file_service: FileService):
        self.view = MainView(self)
        self.settings = Settings()
        self.__file_service = file_service

    def start(self):
        self.view.open()

    #region File methods
    def import_file(self):
        file_name = self.view.get_file()

        self.settings.input_file = file_name
        
        self.view.selected_file_label.config(text=file_name.split('/')[-1])
        
        file_content = self.__file_service.read(file_name)  # Corrigir a chamada do método read
        
        self.process_file(file_content)

    def process_file(self, file_content):
        self.file = file_content

        raw_chapters = self.file.split(SEPARATORS['CHAPTER'])

        [course_title, course_description] = self.get_course_metadata(raw_chapters[0])
        self.course = Course(course_title, course_description)
        self.course.set_chapters(self.get_chapters(raw_chapters[1:]))
    
    def export_file(self):
        if self.settings.output_option == 'File':
            if 'json' in self.settings.output_file:
                with open(self.settings.output_file, 'w', encoding='utf-8') as file:
                    file.write(self.course.to_json())
            elif 'md' in self.settings.output_file:
                with open(self.settings.output_file, 'w', encoding='utf-8') as file:
                    file.write(self.course.to_md())
        elif self.settings.output_option == 'Readwise':
            pass
    #endregion

    #region Model methods
    def get_course_metadata(self, chapter0):
        course_metadata = chapter0.split('\n\n')
        course_title = course_metadata[0].replace(texts[self.settings.language]['course_name'], '')
        course_description = course_metadata[1].replace(texts[self.settings.language]['course_description'], '')
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
            video_title = raw_videos[i].replace('\n', '').replace(texts[self.settings.language]['video'], '')

            video = Video(video_title)
            raw_notes = raw_videos[i + 1].split(SEPARATORS['TIMESTAMP'])[1:]
            video.set_notes(self.get_notes(raw_notes, video.stub))

            videos.append(video)
        return videos

    def get_chapters(self, raw_chapters):
        chapters = []
        for i in range(0, len(raw_chapters), 2):
            chapter_title = raw_chapters[i].replace('\n', '').replace(texts[self.settings.language]['chapter'], '')
            chapter = Chapter(chapter_title)

            raw_videos = raw_chapters[i + 1].split(SEPARATORS['VIDEO'])
            raw_videos = [video for video in raw_videos if video != SEPARATORS['SECTION']]

            chapter.set_videos(self.get_videos(raw_videos))

            chapters.append(chapter)
        return chapters
    #endregion

    #region Getters and Setters
    @property
    def file(self) -> str:
        return self.__file
    
    @file.setter
    def file(self, value: str):
        self.__file = value
    #endregion