"""
@FileName：test.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 15:10
@Copyright：©2018-2024 awesome!
"""
# import gradio as gr
# import time
#
# def my_function(x, progress=gr.Progress()):
#     progress(0, desc="开始...")
#     time.sleep(1)
#     for i in progress.tqdm(range(100)):
#         time.sleep(0.1)
#     return x
#
# gr.Interface(my_function, gr.Textbox(), gr.Textbox()).queue().launch()
import re

if __name__ == '__main__':
    text = """
[
    {"场景1": "在一个古老的东方国度，住着一个名叫阿拉丁的孤儿少年。", "描述1": "一个孤儿少年阿拉丁和他母亲生活在一个古老的东方国度里，他们的生活贫困。"},
    {"场景2": "他与母亲一起生活在贫困之中，阿拉丁不爱学习，也不工作，整日游荡在街头。", "描述2": "少年阿拉丁因为不爱学习和工作，所以一直和母亲生活在贫困之中，并且他整日都在街上游荡。"},
    {"场景3": "一天，阿拉丁的生活中出现了一个自称是他叔叔的陌生人。", "描述3": "阿拉丁的生活中突然出现了一位自称是他叔叔的陌生人。"},
    {"场景4": "这位陌生人实际上是一个来自遥远国度的邪恶魔法师，他寻找神灯已经多年。", "描述4": "突然出现的陌生人其实是一个邪恶魔法师，他一直在寻找传说中的神灯。"},
    {"场景5": "魔法师诱骗阿拉丁帮助他找到神灯，并承诺给予他财富和地位。", "描述5": "邪恶魔法师诱骗无知的阿拉丁帮助自己找到神灯，以获得财富和地位。"},
    {"场景6": "魔法师让阿拉丁下降到洞穴中，取得一盏普通的铜灯和一些宝石。", "描述6": "魔法师要求阿拉丁进入一个洞穴中去取一盏铜灯和一些宝石。"},
    {"场景7": "阿拉丁按照魔法师的指示进入了洞穴，并找到了神灯和其他财宝。", "描述7": "阿拉丁在魔法师的指令下进入了洞穴，并发现了神灯和其他财宝。"},
    {"场景8": "阿拉丁无意中擦了擦神灯，结果召唤出了神灯的守护神灵。", "描述8": "阿拉丁无意中擦亮了神灯，从而召唤出了守护神灵。"},
    {"场景9": "神灵告诉阿拉丁，他可以许三个愿望。", "描述9": "神灯的神灵告诉阿拉丁他可以许三个愿望。"},
    {"场景10": "阿拉丁的第一个愿望是逃出洞穴，神灵立即实现了他的愿望。", "描述10": "阿拉丁的第一个愿望是希望从洞穴中逃脱，神灵立刻帮他实现了愿望。"},
    {"场景11": "回到城市后，阿拉丁没有立即使用第二个愿望，而是开始用洞穴中的宝石改善自己和母亲的生活。", "描述11": "阿拉丁回到城市后没有立即用第二个愿望，而是用洞穴中的宝石开始改善自己和母亲的生活。"},
    {"场景12": "随着时间的推移，阿拉丁被城市中的公主所吸引，并深深地爱上了她。", "描述12": "在城市中，阿拉丁被一位公主所吸引，并且深深地爱上了她。"},
    {"场景13": "他决定使用第二个愿望，希望能够变得富有和有地位，以便能够配得上公主。", "描述13": "为了能配得上公主，阿拉丁决定使用第二个愿望，希望能变得富有和有地位。"},
    {"场景14": "神灵再次实现了他的愿望，阿拉丁变成了城市中最富有、最受尊敬的人。", "描述14": "神灯中的神灵再次实现了他的愿望，使阿拉丁成为了城市中最富有、最受尊敬的人。"},
    {"场景15": "然而，魔法师通过间谍得知了神灯的消息，并设法骗取了阿拉丁的妻子信任，从她手中夺走了神灯。", "描述15": "邪恶的魔法师通过间谍得知了神灯的消息，骗取了阿拉丁妻子的信任，并从她手中夺走了神灯。"},
    {"场景16": "失去了神灯的阿拉丁陷入了绝望，但他并没有放弃。", "描述16": "阿拉丁失去了神灯后陷入了绝望，但他没有放弃。"},
    {"场景17": "通过智慧和勇气，阿拉丁设计了一个计划，成功地从魔法师手中夺回了神灯，并在神灵的帮助下，将魔法师囚禁在了一个遥远的岛屿上。", "描述17": "凭借智慧和勇气，阿拉丁设计了一个计划，成功地从魔法师手中夺回了神灯，并在神灵的帮助下把魔法师囚禁到了一个遥远的岛屿上。"},
    {"场景18": "阿拉丁最终成为了一位英明的国王，他和公主过上了幸福的生活。", "描述18": "最终，阿拉丁成为了一位英明的国王，与公主一起过上了幸福的生活。"},
    {"场景19": "神灯被安全

Process finished with exit code 0

    """
    # # 正则表达式匹配 "场景X": "内容"
    # pattern_view = r'"场景(\d+)":\s*"(.*?)"'
    # pattern_desc = r'"描述(\d+)":\s*"(.*?)"'
    # # 使用 re.DOTALL 使得 '.' 匹配包括换行符在内的所有字符
    # matches_view = re.findall(pattern_view, text, re.DOTALL)
    # extracted_scenes_views = [f'"场景{match[0]}": "{match[1]}"' for match in matches_view]
    # matches_desc = re.findall(pattern_desc, text, re.DOTALL)
    # extracted_scenes_descs = [f'"描述{match[0]}": "{match[1]}"' for match in matches_desc]
    #
    # # 之后我们将关系进行匹配组装，这里用两个倒排表来完成快速匹配
    # views_dict = {}
    # for scenes in extracted_scenes_views:
    #     key,value = scenes.split(":")
    #     key,value = key.replace('"', ''),value.replace('"', '')
    #     views_dict[key]= value
    # descs_dict = {}
    # for scenes in extracted_scenes_descs:
    #     key,value = scenes.split(":")
    #     key, value = key.replace('"', ''), value.replace('"', '')
    #     descs_dict[key]= value
    #
    # res_list = []
    # # 我们将对应的场景和描述联系起来
    # for key,value in views_dict.items():
    #     temp = {}
    #     temp[key] = value
    #     temp["描述"+key[len('场景'):]] = descs_dict.get("描述"+key[len('场景'):],"请手动完善")
    #     res_list.append(temp)
    #
    #
    # # print(extracted_scenes_views,extracted_scenes_descs)
    # print(res_list)

    import gradio as gr
    import pandas as pd


    def start_button_fn(input_text, temperature, prompt_table):
        # 假设我们要在 'Storyboard' 列的末尾添加一行值为 25
        data = {
            'Prompt': ["New Prompt"],
            'Storyboard': [25],
            'Index': [len(prompt_table.get_value()) + 1]  # 假设 Index 是一个递增的唯一标识符
        }
        n_df = pd.DataFrame(data)

        # 获取当前表格的 DataFrame 数据
        current_df = prompt_table.get_value()

        # 将新行添加到当前 DataFrame
        updated_df = current_df.append(n_df, ignore_index=True)

        # 更新表格组件的值
        prompt_table.update_value(updated_df)


    # 初始 DataFrame 数据
    data = {
        'Prompt': ["Prompt 1", "Prompt 2"],
        'Storyboard': ["Storyboard 1", "Storyboard 2"],
        'Index': [1, 2]
    }
    df = pd.DataFrame(data)

    # 创建 Gradio 应用
    with gr.Blocks() as demo:
        # 表单输入
        input_text = gr.Textbox(label="Input Text")


        # 表格组件
        prompt_table = gr.Dataframe(
            headers=["Prompt", "Storyboard", "Index"],
            value=df,
            interactive=True
        )

        # 按钮，点击时触发 start_button_fn 函数
        start_button = gr.Button("Add '25' to Storyboard")

        # 注册按钮的回调函数，传递表格组件作为参数


    # 启动应用
    demo.launch()
