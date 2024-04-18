"""
@FileName：text2Image.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 23:51
@Copyright：©2018-2024 awesome!
"""
import json

from utils import Config

"""
这里我们使用的接口是第三方中转站，因此对接方式不同。后面等我们的设备更新了
我们可以考虑使用RTX4060ti 16GB 来本地部署SD，然后对接本地的模型，这样的话
不仅没有限制，同时成本也能压缩下去，现在一次API调用需要2毛钱
"""

import requests


api_key = Config.settings.get("image_api_key")

class Text2Image():
    def __init__(self):
        # 构建请求头
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def get_taskId(self,prompt):
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
            headers=self.headers,
            data=json.dumps(data)
        )

        return response.json()

    #1713283471368561
    def get_Image(self,task_id):
        url = f'https://api.openai-hk.com/fast/mj/task/{task_id}/fetch'

        # 发送GET请求
        response = requests.get(url, headers=self.headers)
        return response.json()


if __name__ == '__main__':
    text2image = Text2Image()
    # task = text2image.get_taskId("a black cat")
    # task_id = task.get("result")
    # print(task,task_id)
    print(text2image.get_Image("1713283927285806"))

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