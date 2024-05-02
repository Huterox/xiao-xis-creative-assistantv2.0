"""
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 8:58
@Copyright：©2018-2024 awesome!
"""
from app.novelMaker.utils import getConfig
from app.novelMaker.webui.novelAssistant import AssistantNovel
from app.novelMaker.webui.novelGenerate import NovelGenerate
from app.novelMaker.webui.novelSettings import NovelSettings

import os
config = getConfig()
import streamlit as st


def run_app_novel():
    tabs = st.tabs([":green[novel助手]", ":blue[novel生成]", ":red[设置]"])
    with tabs[0]:
        assistant = AssistantNovel()
        assistant.page()
    with tabs[1]:
        novelGenerate = NovelGenerate()
        novelGenerate.page()
    with tabs[2]:
        novelSettings = NovelSettings()
        novelSettings.page()

if __name__ == '__main__':
    run_app_novel()