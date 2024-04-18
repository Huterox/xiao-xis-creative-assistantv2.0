"""
@FileName：novel.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 14:22
@Copyright：©2018-2024 awesome!
"""
import io
from PIL import Image

"""
具体生成视频的UI界面
"""
import gradio as gr
import gradio

class NovelComponent:

    def __init__(self,gr:gradio):
        self.gr:gradio = gr

    def create(self):
        # 最外面分左右两侧，左侧是文本输入，参数调整，右侧是生成的效果展示，微调
        with gr.Row():
            with gr.Column(scale=5):
                self.text_input = gr.Textbox(lines=20,
                                             placeholder="请输入小说文本🎈",
                                             label="文本输入"
                                             )
                with gr.Row():
                    self.temperature = gr.Slider(
                        minimum=0.1, maximum=1, step=0.05, label="temperature",
                        value=0.3,
                        scale=15
                    )

                    self.start_button = gr.Button("模板生成", variant="primary",scale=4,
                                                  min_width=10,size="sm"
                                                  )

            with gr.Column(scale=15):
                with gr.Row():
                    with gr.Column(scale=10,min_width=10):
                        # 说明
                        gr.Text("当前版本直接生成视频，后续增加对简映模板的支持",
                                scale=10,
                                container = False
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
                            scale=2,
                            choices=["ZH-CN-小艺","ZH-CN-云建","ZH-CN-云溪",
                                     "ZH-CN-云霞","ZH-CN-云阳","ZH-CN-辽宁-小北",
                                     "ZH-CN-陕西-小妮"
                                     ],
                        )


                with gr.Column() as dataTable:
                    dataTable.style = "height: 600px; overflow-y: auto;"
                    gr.Text("生成片段（可进行手动调整）：",
                            container=False,
                            )
                    # 接下来这里会成为一组列表
                    imageCard = ImageCard(
                        image_path=r"F:\projects\MatchPro\NovelMaker\assert\img\1.jpg",
                        audio_path=r"F:\projects\MatchPro\NovelMaker\handler\test01.mp3",
                        prompt="Prompt 1",
                        storyboard="Storyboard 1",
                        index=1
                    )
                    imageCard.play()
                    imageCard = ImageCard(
                        image_path=r"F:\projects\MatchPro\NovelMaker\assert\img\2.jpg",
                        audio_path=r"F:\projects\MatchPro\NovelMaker\handler\test01.mp3",
                        prompt="Prompt 1",
                        storyboard="Storyboard 1",
                        index=2
                    )
                    imageCard.play()
                    imageCard = ImageCard(
                        image_path=r"F:\projects\MatchPro\NovelMaker\assert\img\3.jpg",
                        audio_path=r"F:\projects\MatchPro\NovelMaker\handler\test01.mp3",
                        prompt="Prompt 1",
                        storyboard="Storyboard 1",
                        index=3
                    )
                    imageCard.play()


"""
图片展示Card组件，里面包含图像，提示词，分镜，删除，生成按钮
"""
class ImageCard(object):

    def __init__(self, image_path, audio_path,prompt, storyboard, show=True,index=0):

        self.index = index
        self.show = show
        self.image_path = image_path
        self.audio_path = audio_path
        self.prompt_text = prompt
        self.storyboard_text = storyboard
        self.delete_button = None
        self.generate_button = None

    def read_local_image(self)->Image:
            # 读取图片文件
            with open(self.image_path, "rb") as image_file:
                image_data = image_file.read()
            # 使用BytesIO来模拟一个文件对象
            image = Image.open(io.BytesIO(image_data))
            return image

    def play(self):
        if(self.show):
            with gr.Row():
                self.prompt = gr.Textbox(
                    label="ImagePrompt-"+str(self.index),scale=4,min_width=10,
                    value=self.prompt_text,
                    interactive=True
                )
                self.image = gr.Image(
                    label="图像",scale=4,min_width=10,
                    height=100,width=100,
                    value=self.read_local_image()
                ),
                self.storyboard = gr.Textbox(
                    label="配文",scale=4,min_width=10,
                    value=self.storyboard_text,
                    interactive=True
                )
                self.generate_audio = gr.Audio(value=self.audio_path,scale=4,
                                               min_width=10,label="配音",
                                                type="filepath"
                                               )
                self.delete_button = gr.Button(
                    value="生成", variant="primary",scale=1,min_width=10

                )
                self.delete_button = gr.Button(
                    value="删除",variant="stop",scale=1,min_width=10
                )

    def delete(self):
        self.show = False
        del self
