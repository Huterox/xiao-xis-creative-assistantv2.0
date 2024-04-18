"""
@FileName：setting.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/17 15:43
@Copyright：©2018-2024 awesome!
"""
import json

import gradio
import gradio as gr
from utils import Config
import os

class SettingComponent(object):

    def __init__(self,gr:gradio):
        self.gr:gradio = gr
        # config 是引用传递

    def save_settings(self,openai_key, base_url, default_model,
                      mj_api_key, global_temperature)->None:

        Config.settings["openai_api_key"] = openai_key
        Config.settings["openai_api_base"] = base_url
        Config.settings["default_model"] = default_model
        Config.settings["image_api_key"] = mj_api_key
        Config.settings["temperature"] = global_temperature
        # 持久层更新，虽然是在main.py当中调用，但是读取到的还是在webui下面的
        # 不更新文件，只在当前有效
        # current_file_path = os.path.abspath(__file__)
        # current_dir = os.path.dirname(current_file_path)
        # json_data = json.dumps(Config.settings, indent=4,ensure_ascii=False)
        # with open(current_dir + "/../config.json", 'w', encoding='utf-8') as json_file:
        #     json_file.write(json_data)

    def create(self)->None:
        with gr.Blocks(title="设置你的key"):

            with gr.Row():
                # 左侧是设置
                with gr.Column():
                    gr.Label(value="😎TTS语音生成采用EdgeTTS✔，设置仅本次使用生效😁",container=False)
                    self.openai_key = gr.Textbox(lines=1,label="openai key",
                                                 placeholder="请输入你的openai key",
                                                 value=Config.settings.get("openai_api_key"),
                                                 interactive = True
                                                 )
                    self.base_url = gr.Textbox(lines=1,label="base url",
                                               placeholder="请输入你的base url",
                                               value=Config.settings.get("openai_api_base"),
                                               interactive=True
                                               )
                    self.default_model = gr.Textbox(lines=1,label="default model",
                                                    placeholder="请输入你的default model",
                                                    value=Config.settings.get("default_model"),
                                                    interactive=True
                                                    )
                    self.mj_api_key = gr.Textbox(lines=1,label="绘画api_key",
                                                 placeholder="请输入你的绘画api_key",
                                                 value=Config.settings.get("image_api_key"),
                                                 interactive=True
                                                 )

                    self.global_temperature = gr.Number(label="全局temperature",
                                                 maximum=1.0,
                                                 minimum=0.1,
                                                 step=0.1,
                                                 value=Config.settings.get("temperature"),
                                                 interactive=True
                                                 )

                    self.save_button = gr.Button(value="保存设置")
                    # self.save_button.click(fn=self.save_fn)
                    self.save_button.click(fn=self.save_settings,inputs=[self.openai_key,self.base_url,
                                                                         self.default_model,self.mj_api_key,
                                                                         self.global_temperature
                                                                         ],)
                with gr.Column():
                    # 右侧是关于音频的试听
                    gr.Label(value="语音试听😋", container=False)
                    with gr.Row():
                        self.generate_audio = gr.Audio(value=r"F:\projects\MatchPro\NovelMaker\handler\test01.mp3",
                                                       scale=4,
                                                       min_width=10, label="ZH-CN-小艺",
                                                       type="filepath"
                                                       )
                        self.generate_audio = gr.Audio(value=r"F:\projects\MatchPro\NovelMaker\handler\test02.mp3",
                                                       scale=4,
                                                       min_width=10, label="ZH-CN-云建",
                                                       type="filepath"
                                                       )
                        self.generate_audio = gr.Audio(value=r"F:\projects\MatchPro\NovelMaker\handler\test03.mp3",
                                                       scale=4,
                                                       min_width=10, label="ZH-CN-云溪",
                                                       type="filepath"
                                                       )
                        self.generate_audio = gr.Audio(value=r"F:\projects\MatchPro\NovelMaker\handler\test04.mp3",
                                                       scale=4,
                                                       min_width=10, label="ZH-CN-云霞",
                                                       type="filepath"
                                                       )
                    with gr.Row():

                        self.generate_audio = gr.Audio(value=r"F:\projects\MatchPro\NovelMaker\handler\test05.mp3",
                                                       scale=4,
                                                       min_width=10, label="ZH-CN-云阳",
                                                       type="filepath"
                                                       )
                        self.generate_audio = gr.Audio(value=r"F:\projects\MatchPro\NovelMaker\handler\test06.mp3",
                                                       scale=4,
                                                       min_width=10, label="ZH-CN-辽宁-小北",
                                                       type="filepath"
                                                       )
                        self.generate_audio = gr.Audio(value=r"F:\projects\MatchPro\NovelMaker\handler\test07.mp3",
                                                       scale=4,
                                                       min_width=10, label="ZH-CN-陕西-小妮",
                                                       type="filepath"
                                                       )



