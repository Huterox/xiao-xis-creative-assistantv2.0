# 项目简介
 By Huterox is making a tool for novel.
 
# 开发日志

    - 2024-4-17 完成基本页面编写，基本组件库完善

    - 更换暗月之面的API:"openai_api_key": "sk-FGivAMvTnxPSWlp7HrGfDGY8FEHtw1M5w3dHnrqUwzZp29mD",
                     :"openai_api_base": "https://api.moonshot.cn/v1",
                     :"default_model": "moonshot-v1-8k",
    - 这里由于兼容性的问题，修改了pyplot.py 的源码 （T343Line）
            canvas_class = module.FigureCanvasAgg
            FigureCanvasQTAgg = module.FigureCanvasQTAgg
    - 2024-4-18 页面全部重构，在考虑采用Gradio没有考虑到提供组件无法满足设计需求
        - 重新进行页面需求分析，技术调研，决定基于streamlit在现有架构上继续重构
        - 当前版本，保留 -v0.1
        - 等待重构项目，项目版本命名为 -v0.2
     2024-4-19 完成重构-v0.2.0 对首页，novel助手进行重构
                -v0.2.1 完成设置页面重构

