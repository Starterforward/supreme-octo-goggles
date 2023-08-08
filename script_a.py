import os
import subprocess

# Set the full path to the yt-dlp and FFmpeg executables
yt_dlp_path = os.path.join(os.path.dirname(__file__), 'yt-dlp')
ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg')

# Download a video using yt-dlp
subprocess.run([yt_dlp_path, '-o', 'video.mp4', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'])

# Convert the video to another format using FFmpeg
subprocess.run([ffmpeg_path, '-i', 'video.mp4', 'video.avi'])
