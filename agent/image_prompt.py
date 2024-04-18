"""
@FileName：image_prompt.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 22:35
@Copyright：©2018-2024 awesome!
"""
import json
import typing

from openai import OpenAI

from agent.prompt_template import ExtractSegmentNovel, ToImagePrompt
from utils import Config

"""
将小说进行分段
"""

api_key = Config.settings.get("openai_api_key")
client = OpenAI(api_key=api_key,base_url=Config.settings.get("openai_api_base"))

class ImagePromptAgent(object):

    def __send(self,message:typing.List,prompt:typing.List)->typing.AnyStr:
        history_openai_format = [
            {"role": "system",
             "content":prompt
            },
            {"role": "user",
             "content": message
             },
        ]
        completion = client.chat.completions.create(
            model=Config.settings.get("default_model"),
            messages=history_openai_format,
            # 这里需要可能需要一约束
            temperature=0.4,
        )
        result = completion.choices[0].message.content
        return result

    def ExtractSegmentNovel(self,message):
        scenes_list = json.loads(self.__send(message,ExtractSegmentNovel))
        return scenes_list

    def ToImagePrompt(self,message):
        english_prompt ="best quality,masterpiece,illustration, an extremely delicate and beautiful,extremely detailed,CG,unity,8k wallpaper, "+\
                        self.__send(message,ToImagePrompt)
        return english_prompt


if __name__ == '__main__':
    agent = ImagePromptAgent()
    text = """
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
    # print(agent.ExtractSegmentNovel(text))
    print(agent.ToImagePrompt("在一个金碧辉煌的王座大厅中，一个英俊的国王正坐在王座上，他的旁边是一位美丽的王后，他们的脸上都洋溢着幸福和满足的笑容，而在一个隐秘的角落里，一个铜灯静静地躺在那里。"))
