"""
@FileName：storyboardHandler.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/18 9:54
@Copyright：©2018-2024 awesome!
"""
import asyncio
import os
import re
import uuid
from datetime import datetime
import edge_tts

from agent.image_prompt import ImagePromptAgent
from handler.text2Image import Text2Image

"""
######################################################################
****************************在这里处理分镜******************************
######################################################################
"""


class StoryBoardHandler(object):
    def __init__(self):
        # 专门处理分镜的Agent
        self.agentStoryBoard = ImagePromptAgent()
        self.text2image = Text2Image()
        self.voice_map = {
            "小艺":"zh-CN-XiaoyiNeural", "云建":"zh-CN-YunjianNeural",
            "云溪":"zh-CN-YunxiNeural", "云霞":"zh-CN-YunxiaNeural",
            "云阳":"zh-CN-YunyangNeural", "小北":"zh-CN-liaoning-XiaobeiNeural",
            "小妮":"zh-CN-shaanxi-XiaoniNeural"
        }
        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)
        self.resource_dir = self.current_dir+"/../resource"

    # 将返回的结果解析成正常的符合要求的字典，LLM返回的格式并没有严格按照格式返回
    def __extract_json(self,text):
        pattern_view = r'"场景(\d+)":\s*"(.*?)"'
        pattern_desc = r'"描述(\d+)":\s*"(.*?)"'
        # 使用 re.DOTALL 使得 '.' 匹配包括换行符在内的所有字符
        matches_view = re.findall(pattern_view, text, re.DOTALL)
        extracted_scenes_views = [f'"场景{match[0]}": "{match[1]}"' for match in matches_view]
        matches_desc = re.findall(pattern_desc, text, re.DOTALL)
        extracted_scenes_descs = [f'"描述{match[0]}": "{match[1]}"' for match in matches_desc]

        # 之后我们将关系进行匹配组装，这里用两个倒排表来完成快速匹配
        views_dict = {}
        for scenes in extracted_scenes_views:
            key, value = scenes.split(":")
            key, value = key.replace('"', ''), value.replace('"', '')
            views_dict[key] = value
        descs_dict = {}
        for scenes in extracted_scenes_descs:
            key, value = scenes.split(":")
            key, value = key.replace('"', ''), value.replace('"', '')
            descs_dict[key] = value

        res_list = []
        # 我们将对应的场景和描述联系起来
        for key, value in views_dict.items():
            temp = {}
            temp[key] = value
            temp["描述" + key[len('场景'):]] = descs_dict.get("描述" + key[len('场景'):], "请手动完善")
            res_list.append(temp)

        return res_list
    """
    输入文本，得到我们Agent处理之后的分镜描述,这里面做了很多解析的处理
    """
    def getProgressHandler(self,text,temperature=0.4):
        data = self.__extract_json(self.agentStoryBoard.ExtractSegmentNovel(text,temperature))
        return data

    """
    将文本提示词转化为图片
    """
    def getText2Img(self,prompt):
        # 先得到英文的提示词
        prompt = self.agentStoryBoard.ToImagePrompt(prompt)
        # 然后去请求得到图片
        img = self.text2image.text2image(prompt)
        if(img):
            img_path = self.__create_img_stream()
            img.save(img_path)
            return img_path
        return -1

    async def __amain(self,stream,text,voice) -> None:
        """异步处理拿到语音"""
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(stream)

    def text2Audio(self,stream,text,voice):
        # 获取语音，这里的话比较特殊需要使用到协程拿到语音
        loop = asyncio.new_event_loop()
        try:
            # 在这个事件循环中运行amain协程
            loop.run_until_complete(self.__amain(stream,text,voice))
        finally:
            # 关闭事件循环
            loop.close()

    def __create_img_stream(self):

        now = datetime.now()
        year_month_day = now.strftime("%Y%m%d")
        file_uuid = uuid.uuid4()
        audio_stream = self.resource_dir + "/img" + "/" + year_month_day + "/"
        if (not os.path.exists(audio_stream)):
            os.makedirs(audio_stream)
        audio_stream += file_uuid.hex + ".jpg"
        return audio_stream

    def __create_stream(self):
        now = datetime.now()
        year_month_day = now.strftime("%Y%m%d")
        file_uuid = uuid.uuid4()
        audio_stream = self.resource_dir+"/audio"+"/"+year_month_day+"/"
        if( not os.path.exists(audio_stream)):
            os.makedirs(audio_stream)
        audio_stream += file_uuid.hex+".mp3"
        return audio_stream

    """
    将文本转化为音频,返回流对象，可以直接进行在st上展示（重点是在内存里面）
    """
    def getText2Audio(self,text,voice,mode="中文"):
        voice = self.voice_map.get(voice,"zh-CN-XiaoyiNeural")
        if mode == "中文":
            text = text
        else:
            text = self.agentStoryBoard.ToEnglish(text)
        try:
            audio_stream = self.__create_stream()
            self.text2Audio(audio_stream,text,voice)
        except Exception as e:
            print(e)
            audio_stream = -1
        return audio_stream

if __name__ == '__main__':
    storyBoardHandler = StoryBoardHandler()
    # storyBoardHandler.getText2Audio("Hello my name is xiaoyi","小艺","中文")
    # print(storyBoardHandler.getProgressHandler(TEST_TEXT))
    storyBoardHandler.getText2Img("威武霸气的小奶狗")

