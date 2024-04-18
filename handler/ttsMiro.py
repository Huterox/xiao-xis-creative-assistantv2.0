"""
@FileName：ttsMiro.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/17 0:14
@Copyright：©2018-2024 awesome!
"""

import os, requests, time
from xml.etree import ElementTree
import pandas as pd

# 注册申请的微软tts的api——key
# subscription_key = "你的ttskey"
# fetch_token_url = "你的url地址"
# base_url ="含有你的region"
#
# class TextToSpeech(object):
#     def __init__(self, subscription_key,fetch_token_url,base_url):
#         self.subscription_key = subscription_key
#         self.fetch_token_url = fetch_token_url
#         self.base_url = base_url
#         self.tts = "你是最棒的哦，哇哈哈哈"
#         self.timestr = time.strftime("%Y%m%d-%H%M")
#         self.access_token = None
#
#     def get_token(self):
#         headers = {
#             'Ocp-Apim-Subscription-Key': self.subscription_key
#         }
#         response = requests.post(self.fetch_token_url, headers=headers)
#         self.access_token = str(response.text)
#
#     def save_audio(self,data,child_path):
#
#         path = 'cognitiveservices/v1'
#         constructed_url = self.base_url + path
#         headers = {
#             'Authorization': 'Bearer ' + self.access_token,
#             'Content-Type': 'application/ssml+xml',
#             'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
#             'User-Agent': 'TTSForPython'
#         }
#         xml_body = ElementTree.Element('speak', version='1.0')
#         xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
#         voice = ElementTree.SubElement(xml_body, 'voice')
#         voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
#         voice.set('name', 'zh-CN-YunxiNeural')
#         voice.set(' rate ', '1.4')
#         voice.text = data
#         body = ElementTree.tostring(xml_body)
#         response = requests.post(constructed_url, headers=headers, data=body)
#         if response.status_code == 200:
#             with open(child_path+'.wav', 'wb') as audio:
#                 audio.write(response.content)
#                 # print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
#         else:
#             print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
#             print("Reason: " + str(response.reason) + "\n")
#
#     def get_voices_list(self):
#         path = 'cognitiveservices/voices/list'
#         constructed_url = self.base_url + path
#         headers = {
#             'Authorization': 'Bearer ' + self.access_token,
#         }
#         response = requests.get(constructed_url, headers=headers)
#         if response.status_code == 200:
#             print("\nAvailable voices: \n" + response.text)
#         else:
#             print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
#
#
#
# if __name__ == "__main__":


"""
这里只看支持中文的就好了

Name: zh-CN-XiaoyiNeural
Gender: Female

Name: zh-CN-YunjianNeural
Gender: Male

Name: zh-CN-YunxiNeural
Gender: Male

Name: zh-CN-YunxiaNeural
Gender: Male

Name: zh-CN-YunyangNeural
Gender: Male

Name: zh-CN-liaoning-XiaobeiNeural
Gender: Female

Name: zh-CN-shaanxi-XiaoniNeural
Gender: Female
"""

import asyncio

import edge_tts

# TEXT = "大家好，这里是小汐AI助手，请问有什么能够帮助你的呢"
TEXT ="""
    在一个古老的东方国度，住着一个名叫阿拉丁的孤儿少年。他与母亲一起生活在贫困之中，阿拉丁不爱学习，也不工作，整日游荡在街头。

    一天，阿拉丁的生活中出现了一个自称是他叔叔的陌生人。这位陌生人实际上是一个来自遥远国度的邪恶魔法师，他寻找神灯已经多年。魔法师通过魔法得知，只有阿拉丁才能取得那盏神灯。
    
    魔法师诱骗阿拉丁帮助他找到神灯，并承诺给予他财富和地位。他带阿拉丁来到了一个偏远的地方，那里有一个被魔法封印的洞穴。魔法师让阿拉丁下降到洞穴中，取得一盏普通的铜灯和一些宝石。
    
    阿拉丁按照魔法师的指示进入了洞穴，并找到了神灯和其他财宝。但在他准备离开时，洞穴的入口突然关闭，阿拉丁被困在了里面。在绝望中，阿拉丁无意中擦了擦神灯，结果召唤出了神灯的守护神灵。神灵告诉阿拉丁，他可以许三个愿望。
    
    阿拉丁的第一个愿望是逃出洞穴，神灵立即实现了他的愿望。回到城市后，阿拉丁没有立即使用第二个愿望，而是开始用洞穴中的宝石改善自己和母亲的生活。
    
    随着时间的推移，阿拉丁被城市中的公主所吸引，并深深地爱上了她。他决定使用第二个愿望，希望能够变得富有和有地位，以便能够配得上公主。神灵再次实现了他的愿望，阿拉丁变成了城市中最富有、最受尊敬的人。
    
    阿拉丁的财富和魅力最终赢得了公主的芳心，他们相爱并准备结婚。然而，魔法师通过间谍得知了神灯的消息，并设法骗取了阿拉丁的妻子信任，从她手中夺走了神灯。
    
    失去了神灯的阿拉丁陷入了绝望，但他并没有放弃。他决定要夺回神灯，并救回他的妻子。通过智慧和勇气，阿拉丁设计了一个计划，成功地从魔法师手中夺回了神灯，并在神灵的帮助下，将魔法师囚禁在了一个遥远的岛屿上。
    
    阿拉丁最终成为了一位英明的国王，他和公主过上了幸福的生活。神灯被安全地隐藏起来，以防再次落入邪恶之人的手中。这个故事告诉我们，真正的幸福和成功不是靠魔法和奇迹，而是靠个人的勇气、智慧和坚持不懈的努力。
    """
# VOICE = "zh-CN-XiaoyiNeural"
# VOICE = "zh-CN-YunjianNeural"
# VOICE = "zh-CN-YunxiNeural"
# VOICE = "zh-CN-YunxiaNeural"
# VOICE = "zh-CN-YunyangNeural"
# VOICE = "zh-CN-liaoning-XiaobeiNeural"
VOICE = "zh-CN-shaanxi-XiaoniNeural"
OUTPUT_FILE = "test07.mp3"


async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()
