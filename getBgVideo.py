import math
import soundfile as sf
import random
import cv2


def get_audio_length(file_path):
    audio_data, samplerate = sf.read(file_path)
    length_in_seconds = len(audio_data) / samplerate
    return length_in_seconds


total_length = get_audio_length('./Assets/Audio/title.mp3') + get_audio_length('./Assets/Audio/content.mp3')
total_length = math.ceil(total_length) + 2

video_length = 257

video_start = random.randint(0, video_length - total_length)
video_end = video_start + total_length


def crop_video(input_file, output_file, start_time, end_time):
    video_capture = cv2.VideoCapture(input_file)

    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_file, fourcc, fps, (int(video_capture.get(3)), int(video_capture.get(4))))

    for frame_number in range(start_frame, min(end_frame, frame_count)):
        ret, frame = video_capture.read()
        if not ret:
            break
        output_video.write(frame)

    # Release resources
    video_capture.release()
    output_video.release()


crop_video('./Assets/Minecraft Video.mp4', './Assets/Background/bgVideo.mp4', video_start, video_end)
