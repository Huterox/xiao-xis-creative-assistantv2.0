"""
@FileName：videoBuilder.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/21 21:09
@Copyright：©2018-2024 awesome!
"""
import os
import uuid
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, VideoFileClip

class VideoBuilder():
    def __init__(self):
        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)
        self.font_path = self.current_dir+"/../assert/font/simsun.ttc"
        self.resource_dir = self.current_dir + "/../resource"
        self.font_size = 20

    def __create_video_stream(self):
        now = datetime.now()
        year_month_day = now.strftime("%Y%m%d")
        file_uuid = uuid.uuid4()
        video_stream = self.resource_dir + "/video" + "/" + year_month_day + "/"
        if (not os.path.exists(video_stream)):
            os.makedirs(video_stream)
        video_stream += file_uuid.hex + ".mp4"
        return video_stream

    def data2Video(self,data):
        return self.__create_video_with_subtitles(data,self.font_path, self.__create_video_stream())

    def __create_video_with_subtitles(self,data, font_path, save_path):
        try:
            video_clips = []
            total_duration = 0
            index = 0
            for item in data:
                img = Image.open(item["图片"])
                width, height = img.size
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(font_path, size=20)
                # 计算一下字幕位置，假设每个字20px
                text_item = item["分段"]
                start_x = (width - len(text_item) * 25) // 2
                # 再算一下要几行
                line = (((len(text_item) * 30) // width) + 1) * 30
                text_position = (start_x, img.size[1] - line)
                draw.text(text_position, text_item, font=font, fill=(255, 255, 255))

                new_path = os.path.splitext(item["图片"])[0] + item["分段"] + "-c.jpg"
                resized_image = img.resize((640, 480), Image.Resampling.LANCZOS)
                resized_image.save(new_path)

                img_clip = ImageClip(new_path)  # 不需要设置fps，因为我们会根据音频时长设置
                audio_clip = AudioFileClip(item["音频"])
                duration = audio_clip.duration
                total_duration += duration
                audio_clip.start = duration * index
                audio_clip.end = total_duration

                img_clip = img_clip.set_duration(duration)  # 设置图片剪辑的持续时间以匹配音频的时长

                video_clip = CompositeVideoClip([img_clip]).set_audio(audio_clip)
                video_clip.start = index * duration
                video_clip.end = total_duration
                video_clip.set_audio(audio_clip)
                video_clips.append(video_clip)
                index += 1

            # 将所有片段合并成一个视频，moviepy会自动计算总时长
            final_clip = CompositeVideoClip(video_clips, size=video_clips[0].size).set_fps(1)
            # 写入视频文件，不需要指定fps，因为我们已经在CompositeVideoClip中设置了
            final_clip.write_videofile(save_path, codec="libx264")
            return save_path
        except Exception as e:
            print(e)
            return -1
