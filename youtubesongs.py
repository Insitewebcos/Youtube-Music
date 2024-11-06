import yt_dlp
import os

def descargar_audio_youtube(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(os.path.expanduser("~"), "Desktop", '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Prueba con la URL de YouTube
# python C:\\Users\\mdesc\\Desktop\\Youtube\\youtubesongs.py
url = input ("¿url de youtube? = ")
#url = "https://www.youtube.com/watch?v=zfz4J9u2ZTc"
descargar_audio_youtube(url)