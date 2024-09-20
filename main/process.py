import moviepy.editor as mp
import os

# Function to merge videos
def merge_videos(video_paths, output_path):
    try:
        clips = [mp.VideoFileClip(video) for video in video_paths]
        final_clip = mp.concatenate_videoclips(clips)
        final_clip.write_videofile(output_path)
        return output_path
    except Exception as e:
        return f"An error occurred while merging videos: {e}"

# Function to trim a video
def trim_video(video_path, start_time, end_time, output_path):
    try:
        video = mp.VideoFileClip(video_path).subclip(start_time, end_time)
        video.write_videofile(output_path)
        return output_path
    except Exception as e:
        return f"An error occurred while trimming the video: {e}"

# Example to improve the quality of video (you can use ffmpeg or moviepy adjustments)
def improve_video_quality(input_path, output_path, resolution='720p'):
    try:
        video = mp.VideoFileClip(input_path)
        # Modify the video as per quality improvement logic
        video = video.resize(height=720)  # Adjust resolution
        video.write_videofile(output_path)
        return output_path
    except Exception as e:
        return f"An error occurred while improving video quality: {e}"

