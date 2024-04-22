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
                -v0.2.2 完成重构之前的工作量，恢复编码进度
                -v0.2.3 完成模板导出功能，当前由于本身异常，不支持提示词编辑，后期再修复
                -v0.2.4 修复先前异常，恢复提示词编辑功能，
                    同时完成如下功能：
                        - 完成模板导出功能
                        - 完成视频导出工程
                        - 完成新增模板功能
                        - 完成删除单项模板
                        - 剪映模板生成解析
                    预计目标：
                        - 模板解析生成
                        - 导出功能
                -v0.2.5 导出剪映模板的兼容性较差，当前仅支持windows版本，并且
                        对应导出的模板仍需要手动设置字幕，因此这里选择修改方案，导出素材
                        此时由用户将素材导入到剪映or其他的剪辑软件，避免兼容适配问题，后续
                        定制版本考虑增加对模板导出的功能，并且将针对操作系统进行适配。


