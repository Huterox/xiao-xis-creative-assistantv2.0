"""
@FileName：novel.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 14:22
@Copyright：©2018-2024 awesome!
"""
import io
import os

import pandas
import pandas as pd
from PIL import Image

"""
具体生成视频的UI界面
"""
import gradio as gr
import gradio


class ProgressImageCard(gr.Blocks):
    def __init__(self, image_path, audio_path, prompt, storyboard, show=True, index=0, **kwargs):
        with gr.Blocks(**kwargs) as self.root:
            self.index = index
            self.show = show
            self.image_path = image_path
            self.audio_path = audio_path
            self.prompt_text = prompt
            self.storyboard_text = storyboard

            with gr.Row():
                self.image = gr.Image(
                    label="图像", scale=4, min_width=10,
                    height=100, width=100,
                    value=self.read_local_image()
                )

                self.generate_audio = gr.Audio(value=self.audio_path, scale=4,
                                               min_width=10, label="配音",
                                               type="filepath"
                                               )

                self.prompt = gr.Textbox(
                    label="ImagePrompt-" + str(self.index), scale=4, min_width=10,
                    value=self.prompt_text,
                    interactive=True
                )

                self.storyboard = gr.Textbox(
                    label="配文", scale=4, min_width=10,
                    value=self.storyboard_text,
                    interactive=True
                )

                self.chose_tts_current = gr.Dropdown(
                    label="语音选择",
                    min_width=10,
                    scale=2,
                    choices=["小艺", "云建", "云溪",
                             "云霞", "云阳", "小北",
                             "小妮"
                             ],
                    value="小艺",
                    interactive=True
                )

                self.generate_button = gr.Button(
                    value="生成", variant="primary", scale=1, min_width=10
                )
                self.delete_button = gr.Button(
                    value="删除", variant="stop", scale=1, min_width=10
                )

        super().__init__(self.root)

        # 为按钮添加点击事件
        # self.generate_button.click(fn=self.generate,
        #                            inputs=[self.prompt, self.storyboard, self.chose_tts_current])
        # self.delete_button.click(fn=self.delete)

    def read_local_image(self):
        with open(self.image_path, "rb") as f:
            image = Image.open(io.BytesIO(f.read()))
        return image

    def generate(self, prompt, storyboard, chose_tts_current):
        print(f"Generating for {prompt} with storyboard {storyboard}")
        return "Generated output"

    def delete(self):
        self.show = False
        # 删除逻辑，可能需要从 UI 中移除组件或执行其他操作



class NovelComponent:

    def __init__(self,gr:gradio):
        self.gr:gradio = gr
        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)

    def create_progress_image_card(self,image_path, audio_path, prompt, storyboard, index):
        return ProgressImageCard(image_path=image_path, audio_path=audio_path, prompt=prompt, storyboard=storyboard,
                                 index=index)

    def start_button_fn(self, input_text, temperature,df:pd.DataFrame):

        # 这里拿到了df，接下来对里面的参数进行处理
        # 获取当前的 DataFrame 数据
        # 假设我们要在 'Storyboard' 列的末尾添加一行值为 25
        # data = {
        #     'Prompt': ["1"],
        #     'Storyboard': ["1"],
        #     'Index': ["1"],
        # }
        # n_df = pd.DataFrame(data)
        # self.prompt_table.value = n_df
        # self.prompt_table.render()

        # 假设我们要在 'Storyboard' 列的末尾添加一行值为 25
        data = {
            'Prompt': ["New Prompt"],
            'Storyboard': [25],
            'Index': [2]  # 假设 Index 是一个递增的唯一标识符
        }
        n_df = pd.DataFrame(data)



    def create(self):
        # 最外面分左右两侧，左侧是文本输入，参数调整，右侧是生成的效果展示，微调
        with gr.Row() as go:
            with gr.Column(scale=5):
                self.text_input = gr.Textbox(lines=20,
                                             placeholder="请输入小说文本🎈",
                                             label="文本输入"
                                             )
                with gr.Row():
                    self.temperature = gr.Slider(
                        minimum=0.1, maximum=1, step=0.05, label="temperature",
                        value=0.3,
                        scale=15,
                        interactive=True
                    )

                    self.start_button = gr.Button("模板生成", variant="primary",scale=4,
                                                  min_width=10,size="sm"
                                                  )


            with gr.Column(scale=15):
                with gr.Row():
                    with gr.Column(scale=10,min_width=10):
                        with gr.Row():
                            # 说明
                            gr.Text("当前版本直接生成视频，后续增加对简映模板的支持",
                                    scale=30,
                                    container = False
                                    )

                            self.addImageCom = gr.Button("添加场景",
                                                         min_width=1,
                                                         variant="primary",
                                                         scale=1
                                                         )

                    with gr.Column(scale=2,min_width=10):
                        self.change_fix_botton = gr.Button("批量修改",
                                                            variant="secondary",
                                                            min_width=10,
                                                            scale=2
                                                           )
                        self.export_botton_video = gr.Button("视频导出",
                                                       variant="primary",
                                                       min_width=10,
                                                       scale=2
                                                       )
                    with gr.Column(scale=2,min_width=10):
                        self.export_botton_jianying = gr.Button("工程导出",
                                                           variant="primary",
                                                           min_width=10,
                                                           scale=2
                                                       )
                        self.chose_tts_human = gr.Dropdown(
                            label="语音选择",
                            min_width=10,
                            scale=3,
                            choices=["ZH-CN-小艺","ZH-CN-云建","ZH-CN-云溪",
                                     "ZH-CN-云霞","ZH-CN-云阳","ZH-CN-辽宁-小北",
                                     "ZH-CN-陕西-小妮"
                                     ],
                            value="ZH-CN-小艺",
                            interactive=True
                        )

                with gr.Column():
                    gr.Text("生成片段（可进行手动调整）：",
                            container=False,
                            )
                    with gr.Blocks() as self.dataTable:
                        self.dataTable.style = "height: 600px; overflow-y: auto;"
                        # temp_audio = self.current_dir + r"\..\assert\audio\test01.mp3"
                        # new_card = self.create_progress_image_card(
                        #     image_path=r"F:\projects\MatchPro\NovelMaker\assert\img\1.jpg",
                        #     audio_path=temp_audio,
                        #     prompt="Prompt 1",
                        #     storyboard="Storyboard 1",
                        #     index=1
                        # )
                        # gr.Dataset(new_card, None)
                        data = {
                            'Prompt': ["1"],
                            'Storyboard': ["1"],
                            'Index': ["1"],
                        }
                        df = pd.DataFrame(data)
                        self.prompt_table = gr.Dataframe(
                            headers=["Prompt", "Storyboard", "Index"],
                            label="模板",
                            value=df,
                            interactive=True
                        )
        # 添加按钮的绑定事件
        self.start_button.click(self.start_button_fn, inputs=[self.text_input, self.temperature,
                                                              self.prompt_table
                                                              ])


