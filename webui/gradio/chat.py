"""
@FileName：helperChat.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 10:00
@Copyright：©2018-2024 awesome!
"""
import gradio
import gradio as gr
from handler.helperChat import ChatBotHandler
"""
chatbot组件，负责ui展示，逻辑由handler提供
"""
from typing import Callable, Union


class ChatBotComponent:

    def __init__(self,gr:gradio):
        self.gr:gradio = gr
        self.respond:Callable

    def set_response(self,respond:Union[Callable,ChatBotHandler])->None:
        if isinstance(respond,ChatBotHandler):
            self.respond = respond.chat
        self.respond = respond

    def set_streamBot(self,handler:ChatBotHandler):
        self.user_stream = handler.user_stream
        self.bot_stream = handler.bot_stream

    def creat(self)->None:
        # 先水平放置左右边栏
        with self.gr.Blocks() as d:
            chatbot = gr.Chatbot(
                label = "对话框",
                placeholder="🍭🍡你好！我是全能创作助手~小汐🥰，可以帮助您完善补充文案细节？🧐"
                                 )
            msg = self.gr.Textbox(label="输入框")
            clear = self.gr.ClearButton([msg, chatbot],value = "清除",)
            # 绑定输入框内的回车键的响应函数
            # msg.submit(self.respond, [msg, chatbot], [msg, chatbot])

            msg.submit(self.user_stream, [msg, chatbot], [msg, chatbot], queue=False).then(
                self.bot_stream, chatbot, chatbot
            )
            clear.click(lambda: None, None, chatbot, queue=False)