"""
@FileName：text2Image.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 23:51
@Copyright：©2018-2024 awesome!
"""
import json
import os
import time
import uuid
from datetime import datetime
from io import BytesIO

from utils import Config

"""
这里我们使用的接口是第三方中转站，因此对接方式不同。后面等我们的设备更新了
我们可以考虑使用RTX4060ti 16GB 来本地部署SD，然后对接本地的模型，这样的话
不仅没有限制，同时成本也能压缩下去，现在一次API调用需要2毛钱
"""

import requests
from PIL import Image

api_key = Config.settings.get("image_api_key")

class Text2Image():
    def __init__(self):
        # 构建请求头
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)
        self.resource_dir = self.current_dir+"/../resource"

    def get_taskId(self,prompt):

        def send(prompt,headers):
            data = {
                "base64Array": [],
                "instanceId": "",
                "modes": [],
                "notifyHook": "https://ww.baidu.com/notifyHook/back",
                "prompt": prompt,
                "remix": True,
                "state": ""
            }

            response = requests.post(
                url='https://api.openai-hk.com/fast/mj/submit/imagine',
                headers=headers,
                data=json.dumps(data)
            )
            return response.json()
        try:
            result = send(prompt, self.headers)
        except Exception as e:
            result = {'code':-1}
        if result.get('code') == 1:
            return result.get("result")
        else:
            return None

    #1713283471368561
    def get_Image(self,task_id):
        url = f'https://api.openai-hk.com/fast/mj/task/{task_id}/fetch'

        # 发送GET请求
        response = requests.get(url, headers=self.headers)
        return response.json()

    def __create_img_stream(self):

        now = datetime.now()
        year_month_day = now.strftime("%Y%m%d")
        file_uuid = uuid.uuid4()
        audio_stream = self.resource_dir + "/img" + "/" + year_month_day + "/"
        if (not os.path.exists(audio_stream)):
            os.makedirs(audio_stream)
        audio_stream += file_uuid.hex + ".jpg"
        return audio_stream


    def __getImg(self,url):
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        quarter_width = width // 2
        quarter_height = height // 2
        # 裁剪左上角的四分之一图片
        cropped_image = image.crop((0, 0, quarter_width, quarter_height))
        return cropped_image
        # width, height = cropped_image.size
        # new_height = int((3 / 4) * width)
        # # 使用resize方法调整图片尺寸
        # resized_image = cropped_image.resize((width, new_height), Image.Resampling.LANCZOS)
        # return resized_image

    # 只要这个任务执行失败，那么我们就返回为空
    def text2image(self,prompt):
        # 先拿到task_id
        task_id = self.get_taskId(prompt)
        if(task_id):
            return self.__text2image(prompt,task_id)
        else:
            return None

    def __text2image(self,prompt,task_id):

        res = self.get_Image(task_id)
        # 执行失败
        if(res.get("status")=="FAILURE"):
            return None
        if(res.get('progress') == "100%"):
            return self.__getImg(res.get("imageUrl"))
        else:
            # 还在生成，等待一会再去重试呗,调用api生成还是比较慢的
            time.sleep(2)
            return self.__text2image(prompt,task_id)



if __name__ == '__main__':
    # text2image = Text2Image()
    # task = text2image.get_taskId("a black cat")
    # task_id = task.get("result")
    # print(task,task_id)
    # print(text2image.get_Image("1713283927285806"))

    # print(text2image.text2image("a black cat"))

    image = Image.open(r"F:\projects\MatchPro\NovelMaker\resource\img\20240421\c58237123b824193950c51ebfa29d921.jpg")
    image.show()
    width, height = image.size
    quarter_width = width // 2
    quarter_height = height // 2
    crop_image=image.crop((0,0,quarter_width,quarter_height))

    new = image.resize((400, 300), Image.Resampling.LANCZOS)
    new.show()

    """
    执行成功之后，返回
        response_data = {
        'id': '1713283927285806',
        'properties': {
            'discordChannelId': '1222483390712774667',
            'botType': 'MID_JOURNEY',
            'notifyHook': 'https://www.open-hk.com/openai/mjapi/16158-567/https%3A%2F%2Fww.baidu.com%2FnotifyHook%2Fback',
            'discordInstanceId': '1500442604632883200',
            'flags': 0,
            'messageId': '1229828231935426650',
            'messageHash': 'b1290620-0d25-4882-a72d-102dc174fc22',
            'nonce': '1501375981829570560',
            'finalPrompt': 'a black cat',
            'progressMessageId': '1229827516609331220',
            'messageContent': '**a black cat** - <@1222482757389910027> (fast)'
        },
        'action': 'IMAGINE',
        'status': 'SUCCESS',
        'prompt': 'a black cat',
        'promptEn': 'a black cat',
        'description': '/imagine a black cat',
        'submitTime': 1713283927285,
        'startTime': 1713284128607,
        'finishTime': 1713284300009,
        'progress': '100%',
        'imageUrl': 'https://proxy.xjai.top:33330/mjcdn/attachments/1222483390712774667/1229828230979129374/xizaizai0902_a_black_cat_b1290620-0d25-4882-a72d-102dc174fc22.png?ex=663119cb&is=661ea4cb&hm=1657fcc1bfd3f971fd2d9349ee8b5442a2b300f95e13ab72cee662d76e09789a&',
        'failReason': None,
        'state': '16158',
        'buttons': [
            {
                'customId': 'MJ::JOB::upsample::1::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'U1',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::upsample::2::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'U2',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::upsample::3::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'U3',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::upsample::4::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'U4',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::reroll::0::b1290620-0d25-4882-a72d-102dc174fc22::SOLO',
                'emoji': '🔄',
                'label': '',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::variation::1::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'V1',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::variation::2::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'V2',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::variation::3::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'V3',
                'type': 2,
                'style': 2
            },
            {
                'customId': 'MJ::JOB::variation::4::b1290620-0d25-4882-a72d-102dc174fc22',
                'emoji': '',
                'label': 'V4',
                'type': 2,
                'style': 2
            }
        ]
    }
    """