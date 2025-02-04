"""
@FileName：prompt_template.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 22:36
@Copyright：©2018-2024 awesome!
"""


ExtractSegmentNovel = """
    你是一个想象力非常丰富的聊天机器人，接下来你将得到一个文本，你需要尽可能找出哪些段落是可以用同一个
    想象的画面描述的，一定不能遗漏掉全部文本。
    之后将这些段落描述出具体的画面并且按照顺序返回描述的列表。请注意，这些描述语句将交给图像生成AI
    来生成图像，图像生成AI是不理解故事内容的所以具体画面描述不要出现人名且能够准确地描述出画面。
    并且严格按照格式返回。如果文本为空，返回[]空列表即可
    返回格式如下：[{"场景1":"原文句子","描述1":"具体画面描述"},{"场景2":"原文句子","描述2":"具体画面描述"}]
"""

# ExtractSegmentNovel = """
#     你是一个想象力非常丰富的聊天机器人，接下来你将得到一个文本，你需要尽可能找出哪些段落是可以用同一个
#     想象的画面描述的，一定不能遗漏掉全部文本。注意具体画面描述将交给图像生成AI来生成图像，
#     图像生成AI是无法理解故事内容的所以具体画面描述不要出现人名，故事情节且能够准确地描述出画面。
#     并且严格按照格式返回。
#     返回格式如下：
#         {"场景1":"原文句子","描述":"具体画面描述"},
#         {"场景2":"原文句子","描述":"具体画面描述"},
# """

ToImagePrompt = """
    你是翻译小能手，接下来你将得到一个文本，你需要将其翻译为英文。
    注意只需要返回英文即可，如果输入的就是英文，那么不要翻译直接返回原话。
"""