import json

from functions import unformat, timestamp_to_seconds
from settings import INPUT_FILE, LANGUAGE, OUTPUT_FILE, OUTPUT_FORMAT
from language import texts


LINKEDIN_LEARNING_URL = 'https://www.linkedin.com/learning'
TIMESTAMP_SEPARATOR = '\n0'
CHAPTER_SEPARATOR = '*' * 47
SECTION_SEPARATOR = '\n' * 3
VIDEO_SEPARATOR = '-' * 47
NEW_LINE_SPACING = ' ' * 4
INLINE_SPACING = ' ' * 12


with open(FILE_NAME, 'r', encoding='utf-8') as file:
    notes = file.read()

# Split the content into chapters
chapters = notes.split(CHAPTER_SEPARATOR)

# Extract metadata from "chapter 0"
course_metadata = chapters.pop(0).split('\n\n')
course_title = course_metadata[0].replace(texts[LANGUAGE]['course_name'], '')
course_description = course_metadata[1].replace(texts[LANGUAGE]['course_description'], '')

chapter_list = []
for j in range(0, len(chapters), 2):
    chapter_title = chapters[j].replace('\n', '').replace(texts[LANGUAGE]['chapter'], '')

    # Split the content into videos
    videos = chapters[j + 1].split(VIDEO_SEPARATOR)
    videos = [video for video in videos if video != SECTION_SEPARATOR]

    chapter_videos = []
    for j in range(0, len(videos), 2):
        video_title = videos[j].replace('\n', '').replace(texts[LANGUAGE]['video'], '')

        # FIXME: Doesn't work for 1 hour+ videos
        notes = videos[j + 1].split(TIMESTAMP_SEPARATOR)[1:]

        video_notes = []
        for k in range(len(notes)):
            split_note = notes[k].split(INLINE_SPACING)
            timestamp = f'00{split_note[0]}'
            text = split_note[1].replace(SECTION_SEPARATOR, '').replace(NEW_LINE_SPACING, '')
            video_notes.append({'timestamp': timestamp, 'text': text})

        chapter_videos.append({'title': video_title, 'notes': video_notes})

    chapter_list.append({'title': chapter_title, 'videos': chapter_videos})

course = {
    'title': course_title,
    'description': course_description,
    'chapters': chapter_list
}

parsed_notes = json.dumps(course, indent=2, ensure_ascii=False)

with open('parsed_notes.json', 'w', encoding='utf-8') as file:
    file.write(parsed_notes)