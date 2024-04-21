"""
@FileName：utils.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 22:38
@Copyright：©2018-2024 awesome!
"""
import json
import os
import streamlit as st
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip

"""
这里重新修改为支持streamlit状态保存的方法
"""
def getConfig()->dict:
    try:
        with open(r"./config.json", 'r', encoding="utf-8") as f:
            config = json.load(f)
    except Exception as e:
        try:
            current_file_path = os.path.abspath(__file__)
            current_dir = os.path.dirname(current_file_path)
            with open(current_dir + "/../config.json", 'r', encoding="utf-8") as f:
                config = json.load(f)
        except Exception as e:
            current_file_path = os.path.abspath(__file__)
            current_dir = os.path.dirname(current_file_path)
            with open(current_dir + "/config.json", 'r', encoding="utf-8") as f:
                config = json.load(f)
    if ("settings" in st.session_state.keys()):
        config = st.session_state.settings
    else:
        st.session_state.settings = config
    return config
# config 变为全局变量

class Config(object):
    settings = getConfig()


# 合成视频
data = [
    {
        "字幕": "part1",
        "图片": r"F:\projects\MatchPro\NovelMaker\resource\img\20240421\830c050927e74930bd5a483c71dc438f.jpg",
        "音频": r"F:\projects\MatchPro\NovelMaker\assert\audio\test01.mp3"
    },
    {
        "字幕": "part2",
        "图片": r"F:\projects\MatchPro\NovelMaker\resource\img\20240421\e682e3f2ce5e48b9a2ec667f4da4cfeb.jpg",
        "音频": r"F:\projects\MatchPro\NovelMaker\assert\audio\test01.mp3"
    },
]
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, VideoFileClip

# 字体路径，确保选择一个系统中存在的字体
font_path = r"F:\projects\MatchPro\NovelMaker\assert\font\simsun.ttc"

def create_video_with_subtitles(data, font_path,save_path):
    video_clips = []
    total_duration = 0
    index = 0
    for item in data:
        img = Image.open(item["图片"])
        width, height = img.size
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, size=20)
        # 计算一下字幕位置，假设每个字20px
        text_item = item["字幕"]
        start_x = (width - len(text_item)*25)//2
        # 再算一下要几行
        line = (((len(text_item)*30)//width)+1)*30
        text_position = (start_x, img.size[1] - line)
        draw.text(text_position, text_item, font=font, fill=(255, 255, 255))

        new_path = os.path.splitext(item["图片"])[0] + item["字幕"] + "-c.jpg"
        resized_image = img.resize((640, 480), Image.Resampling.LANCZOS)
        resized_image.save(new_path)

        img_clip = ImageClip(new_path)  # 不需要设置fps，因为我们会根据音频时长设置
        audio_clip = AudioFileClip(item["音频"])
        duration = audio_clip.duration
        total_duration += duration
        audio_clip.start = duration*index
        audio_clip.end = total_duration

        img_clip = img_clip.set_duration(duration)  # 设置图片剪辑的持续时间以匹配音频的时长

        video_clip = CompositeVideoClip([img_clip]).set_audio(audio_clip)
        video_clip.start = index*duration
        video_clip.end = total_duration
        video_clip.set_audio(audio_clip)
        video_clips.append(video_clip)
        index+=1

    # 将所有片段合并成一个视频，moviepy会自动计算总时长
    final_clip = CompositeVideoClip(video_clips, size=video_clips[0].size).set_fps(1)

    # 写入视频文件，不需要指定fps，因为我们已经在CompositeVideoClip中设置了
    final_clip.write_videofile(save_path, codec="libx264")

if __name__ == '__main__':
    create_video_with_subtitles(data, font_path,save_path="output_video_with_subtitles.mp4")