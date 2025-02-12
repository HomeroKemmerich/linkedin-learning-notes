import json

from functions import unformat, timestamp_to_seconds
from settings import INPUT_FILE, LANGUAGE, OUTPUT_FILE, OUTPUT_FORMAT
from language import texts

from models.chapter import Chapter
from models.course import Course
from models.video import Video
from models.note import Note

LINKEDIN_LEARNING_URL = 'https://www.linkedin.com/learning'
TIMESTAMP_SEPARATOR = '\n0'
CHAPTER_SEPARATOR = '*' * 47
SECTION_SEPARATOR = '\n' * 3
VIDEO_SEPARATOR = '-' * 47
NEW_LINE_SPACING = ' ' * 4
INLINE_SPACING = ' ' * 12


#region INPUT
with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    notes = file.read()
#endregion

#region PROCESS
# Split the content into chapters
chapters = notes.split(CHAPTER_SEPARATOR)

# Extract metadata from "chapter 0"
course_metadata = chapters.pop(0).split('\n\n')
course_title = course_metadata[0].replace(texts[LANGUAGE]['course_name'], '')
course_description = course_metadata[1].replace(texts[LANGUAGE]['course_description'], '')
course_stub = course_title.lower().replace(':', '').replace(' ', '-')

chapter_list = []
for j in range(0, len(chapters), 2):
    chapter_title = chapters[j].replace('\n', '').replace(texts[LANGUAGE]['chapter'], '')

    # Split the content into videos
    videos = chapters[j + 1].split(VIDEO_SEPARATOR)
    videos = [video for video in videos if video != SECTION_SEPARATOR]

    chapter_videos = []
    for j in range(0, len(videos), 2):
        video_title = videos[j].replace('\n', '').replace(texts[LANGUAGE]['video'], '')
        video_stub = unformat(video_title.lower().replace(' ', '-')).replace('?', '')

        # FIXME: Doesn't work for 1 hour+ videos
        notes = videos[j + 1].split(TIMESTAMP_SEPARATOR)[1:]

        video_notes = []
        for k in range(len(notes)):
            split_note = notes[k].split(INLINE_SPACING)

            timestamp = f'00{split_note[0]}'
            text = split_note[1].replace(SECTION_SEPARATOR, '').replace(NEW_LINE_SPACING, '')
            url= f'{LINKEDIN_LEARNING_URL}/{course_stub}/{video_stub}?seekTo={timestamp_to_seconds(timestamp)}'

            video_notes.append(Note(timestamp, url, text))

        chapter_videos.append(Video(video_title, video_notes))

    chapter_list.append(Chapter(chapter_title, chapter_videos))

course = Course(course_title, course_description, chapter_list)
#endregion

#region OUTPUT
json_notes = course.to_json()
md_notes = course.to_md()

output = {
    'json': json_notes,
    'md': md_notes
}

with open(f'{OUTPUT_FILE}.{OUTPUT_FORMAT}', 'w', encoding='utf-8') as file:
    file.write(output[OUTPUT_FORMAT])
#endregion