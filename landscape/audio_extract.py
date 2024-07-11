import os
from moviepy.editor import VideoFileClip

# Define paths
video_folder_path = 'train/thunder'  # Update this path
audio_folder_path = 'Audio/thunder'  # Update this path

# Create the audio folder if it doesn't exist
os.makedirs(audio_folder_path, exist_ok=True)

# List all files in the video folder
video_files = [f for f in os.listdir(video_folder_path) if f.endswith(('.mp4', '.avi', '.mkv', '.mov'))]

# Extract audio from each video file
for video_file in video_files:
    video_path = os.path.join(video_folder_path, video_file)
    audio_path = os.path.join(audio_folder_path, f"{os.path.splitext(video_file)[0]}.wav")

    # Load the video file
    video_clip = VideoFileClip(video_path)
    
    # Extract audio
    audio_clip = video_clip.audio
    
    # Write the audio file in .wav format
    audio_clip.write_audiofile(audio_path, codec='pcm_s16le')
    
    # Close the clips
    video_clip.close()
    audio_clip.close()

print("Audio extraction to .wav files is complete!")
