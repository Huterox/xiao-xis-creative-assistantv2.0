# 项目简介
 By Huterox is making a tool for novel.
 
# 开发日志
    - 2024-4-17 完成基本页面编写，基本组件库完善

    - 更换暗月之面的API:"openai_api_key": "sk-FGivAMvTnxPSWlp7HrGfDGY8FEHtw1M5w3dHnrqUwzZp29mD",
                     :"openai_api_base": "https://api.moonshot.cn/v1",
                     :"default_model": "moonshot-v1-8k",
    - 这里由于兼容性的问题，修改了pyplot.py 的源码 （T343Line）
            canvas_class = module.FigureCanvasAgg