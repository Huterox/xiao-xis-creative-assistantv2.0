"""
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 8:58
@Copyright：©2018-2024 awesome!
"""
import json
import os

import gradio as gr

from utils import getConfig
from webui.chat import ChatBotComponent
from handler.helperChat import ChatBotHandler
from webui.novel import NovelComponent
from webui.setting import SettingComponent

my_theme = gr.Theme.load("./theme/miku.json")

config = getConfig()

if __name__ == '__main__':
    os.environ["no_proxy"] = "localhost,127.0.0.1,::1"
    with gr.Blocks(
        title='Novel tweet generator',
        theme=my_theme,
        fill_height = False,
        css="""
        footer {visibility: hidden}
        """,

    ) as demo:
        title = gr.Markdown("#### 创作生成器v0.1-beta（￣︶￣）↗　")
        # 顶部tag导航
        with gr.Tab(label="Novel助手"):
            # chat 对话机器人
            chat = ChatBotComponent(gr)
            # chat.set_response(ChatBotHandler().chat)
            chat.set_streamBot(ChatBotHandler())
            chat.creat()

        with gr.Tab(label="Novel合成"):
            # novel合成
            novel = NovelComponent(gr)
            novel.create()

        with gr.Tab(label="key设置"):
            # 设置页面
            setting = SettingComponent(gr)
            setting.create()

    demo.launch(share=config.get("share",True))
