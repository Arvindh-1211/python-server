import yt_dlp
import os

def download(url, format):  

    output_folder = os.getcwd()  
    # Create a youtube-dl object with download options
    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Customize output filename template if desired
        'format': format, # Choose preferred format (audio, video, best, etc.) with the desired video quality
        'quiet' : True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the file
        ydl.download([url])

    return "File downloaded successfully!"

if __name__ == '__main__':
    download(input("URL: "), 'best')