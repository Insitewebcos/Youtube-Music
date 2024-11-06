# Youtube Music
 Download Youtube Music from url

For the script to work correctly on your PC, you need to have yt-dlp and FFmpeg installed. Here I explain how to install each one and configure it in your PATH.

Install yt-dlp yt-dlp is an improved version of youtube-dl and is responsible for downloading the video and audio. You can install it using pip (Python's package manager). Run in your terminal or command prompt: pip install yt-dlp This will install yt-dlp and allow your script to import it without problems.

Install FFmpeg FFmpeg is an audio and video processing tool that yt-dlp uses to convert downloaded files into audio format (mp3 in this case).

Installation on Windows: Download the FFmpeg package from https://ffmpeg.org/download.html or from the trusted FFmpeg builds site. Extract the downloaded file and place the folder in a convenient location, such as C:\ffmpeg. Add FFmpeg to the PATH: Go to Advanced System Configuration > Environment Variables. Under System Variables, select Path and click Edit. Add the path to the FFmpeg bin folder, for example C:\ffmpeg\bin. Verify the installation by opening a terminal and running: ffmpeg -version

Installation on macOS and Linux: On macOS and Linux, you can install FFmpeg more easily using brew or your system's package manager.

On macOS (with Homebrew installed): brew install ffmpeg

On Linux (Debian/Ubuntu): sudo apt update sudo apt install ffmpeg

Final verification Once yt-dlp and FFmpeg are installed, your script should work correctly. Simply run the script, provide a valid YouTube URL, and the MP3 file will download to your desktop.
