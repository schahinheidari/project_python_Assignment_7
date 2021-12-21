from moviepy import editor

video = editor.VideoFileClip('/home/shahin/Downloads/Video/Iranian.ts')
video.audio.write_audiofile('/home/shahin/Downloads/Video/Iranian.mp3')