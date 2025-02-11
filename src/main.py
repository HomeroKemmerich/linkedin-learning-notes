import json

from constants import FILE_NAME

with open(FILE_NAME, 'r', encoding='utf-8') as file:
    notes = file.read()

# Split the content into chapters
chapters = notes.split('***********************************************')

# Extract metadata from "chapter 0"
course_metadata = chapters.pop(0).split('\n\n')
course_title = course_metadata[0].split('Nome do curso: ')[1]
course_description = course_metadata[1].split('Descrição: ')[1]

chapter_list = []
for j in range(0, len(chapters), 2):
    chapter_title = chapters[j].replace('\n', '')

    videos = chapters[j + 1].split('-----------------------------------------------')
    videos = [video for video in videos if video != '\n\n\n']

    chapter_videos = []
    for j in range(0, len(videos), 2):
        video_title = videos[j].replace('\n', '').replace('Vídeo: ', '')

        notes = videos[j + 1].split('\n0')[1:]

        video_notes = []
        for k in range(len(notes)):
            split_note = notes[k].split('            ')
            timestamp = f'00{split_note[0]}'
            text = split_note[1].replace('\n\n\n', '').replace('    ', '')
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