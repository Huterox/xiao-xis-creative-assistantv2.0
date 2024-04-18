"""
@FileName：storyboardHandler.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/18 9:54
@Copyright：©2018-2024 awesome!
"""
import re

from agent.image_prompt import ImagePromptAgent

"""
######################################################################
****************************在这里处理分镜******************************
######################################################################
"""

TEST_TEXT = """
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

class StoryBoardHandler(object):
    def __init__(self):
        # 专门处理分镜的Agent
        self.agentStoryBoard = ImagePromptAgent()

    # 将返回的结果解析成正常的符合要求的字典，LLM返回的格式并没有严格按照格式返回
    def __extract_json(self,text):
        pattern_view = r'"场景(\d+)":\s*"(.*?)"'
        pattern_desc = r'"描述(\d+)":\s*"(.*?)"'
        # 使用 re.DOTALL 使得 '.' 匹配包括换行符在内的所有字符
        matches_view = re.findall(pattern_view, text, re.DOTALL)
        extracted_scenes_views = [f'"场景{match[0]}": "{match[1]}"' for match in matches_view]
        matches_desc = re.findall(pattern_desc, text, re.DOTALL)
        extracted_scenes_descs = [f'"描述{match[0]}": "{match[1]}"' for match in matches_desc]

        # 之后我们将关系进行匹配组装，这里用两个倒排表来完成快速匹配
        views_dict = {}
        for scenes in extracted_scenes_views:
            key, value = scenes.split(":")
            key, value = key.replace('"', ''), value.replace('"', '')
            views_dict[key] = value
        descs_dict = {}
        for scenes in extracted_scenes_descs:
            key, value = scenes.split(":")
            key, value = key.replace('"', ''), value.replace('"', '')
            descs_dict[key] = value

        res_list = []
        # 我们将对应的场景和描述联系起来
        for key, value in views_dict.items():
            temp = {}
            temp[key] = value
            temp["描述" + key[len('场景'):]] = descs_dict.get("描述" + key[len('场景'):], "请手动完善")
            res_list.append(temp)

        return res_list
    """
    输入文本，得到我们Agent处理之后的分镜描述,这里面做了很多解析的处理
    """
    def getProgressHandler(self,text):
        data = self.__extract_json(self.agentStoryBoard.ExtractSegmentNovel(text))
        return data

if __name__ == '__main__':
    storyBoardHandler = StoryBoardHandler()
    print(storyBoardHandler.getProgressHandler(TEST_TEXT))
