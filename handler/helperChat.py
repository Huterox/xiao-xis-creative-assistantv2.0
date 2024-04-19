"""
@FileName：helperChat.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 10:24
@Copyright：©2018-2024 awesome!
"""

import time
from openai import OpenAI

from utils import Config
api_key = Config.settings.get("openai_api_key")
client = OpenAI(api_key=api_key,base_url=Config.settings.get("openai_api_base"))


class ChatBotHandler(object):
    def __init__(self, bot_name="chat"):
        self.bot_name = bot_name
        self.current_message = None


    def user_stream(self,user_message, history):
        self.current_message = user_message
        return "", history + [[user_message, None]]

    def bot_stream(self,history):

        if(len(history)==0):
            history.append([self.current_message,None])
        bot_message = self.getResponse(history[-1][0],history)
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.02)
            yield history

    def signChat(self,history):
        history_openai_format = []
        # 先加入系统信息
        history_openai_format.append(
            {"role": "system",
             "content": Config.settings.get("system_xiaoxi")
             },
        )
        # 再加入解析信息
        history_openai_format.extend(history)
        # print(history_openai_format)
        completion = client.chat.completions.create(
            model=Config.settings.get("default_model"),
            messages=history_openai_format,
            temperature=Config.settings.get("temperature"),
        )
        result = completion.choices[0].message.content
        return result

    def getResponse(self,message,history):
        history_openai_format = []
        for human, assistant in history:
            # 基础对话的系统设置
            history_openai_format.append(
                {"role": "system",
                 "content":Config.settings.get("system_xiaoxi")
                },
            )
            if(human!=None):
                history_openai_format.append({"role": "user", "content": human})
            if(assistant!=None):
                history_openai_format.append({"role": "assistant", "content": assistant})

        completion = client.chat.completions.create(
            model=Config.settings.get("default_model"),
            messages=history_openai_format,
            temperature=Config.settings.get("temperature"),
        )
        result = completion.choices[0].message.content
        return result


    def chat(self,message, history):
        history_openai_format = []
        for human, assistant in history:
            history_openai_format.append({"role": "user", "content": human})
            history_openai_format.append({"role": "system", "content": assistant})
        history_openai_format.append({"role": "user", "content": message})

        response = client.chat.completions.create(model="moonshot-v1-8k",
                                                  messages=history_openai_format,
                                                  temperature=1.0,
                                                  stream=True)

        partial_message = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                partial_message = partial_message + chunk.choices[0].delta.content
                yield partial_message