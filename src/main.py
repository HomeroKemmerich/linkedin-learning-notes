from constants import FILE_NAME

with open(FILE_NAME, 'r', encoding='utf-8') as file:
    notes = file.read()

# Split the content into chapters
chapters = notes.split('***********************************************')

metadata = chapters.pop(0).split('\n\n')
title = metadata[0].split('Nome do curso: ')[1]
description = metadata[1].split('Descrição: ')[1]

chapter_list = []
for i in range(0, len(chapters), 2):
    video = chapters[i+1].split('\n-----------------------------------------------')
    video = [v for v in video if v != '\n\n']
    video_title = video[0].split('Vídeo: ')[1]
    video_notes = video[1].split('\n')
    video_notes = [n for n in video_notes if n != '']
    video_notes = [n for n in video_notes if n != 'Hora da nota:      Texto da nota:                 ']    
    chapter = {
        'title': chapters[i].replace('\n', ''),
        'videos': chapters[i+1].replace('\n-----------------------------------------------', '')
    }
    chapter_list.append(chapter)

    print(video_notes)
