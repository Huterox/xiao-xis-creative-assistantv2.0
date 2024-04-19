"""
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 8:58
@Copyright：©2018-2024 awesome!
"""

from utils import getConfig
from webui.streamlit.novelAssistant import AssistantNovel
from webui.streamlit.novelGenerate import NovelGenerate
from webui.streamlit.novelSettings import NovelSettings
import os

config = getConfig()
import streamlit as st

def index():

    st.markdown("*Novel-Video创作助手* is **really** ***cool*** --v0.1beta（￣︶￣）↗　.")
    st.markdown('''
        :red[自带] :orange[小汐] :green[创作助手] :blue[完成文档润色] :violet[流水线]
        :gray[内容生成] :rainbow[解放双手].''')
    st.markdown("Welcome to here! &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    st.image(current_dir+r"/assert/img/bg.jpg",width=800)

if __name__ == '__main__':

    def page_content(page):
        if page == ':rainbow[首页]':
            index()
        if page == ':green[novel助手]':
            assistant = AssistantNovel()
            assistant.page()
        elif page == ':blue[novel生成]':
            novelGenerate = NovelGenerate()
            novelGenerate.page()
        elif page == ':red[设置]':
            novelSettings = NovelSettings()
            novelSettings.page()


    custom_css = """
        <style>
        .block-container.st-emotion-cache-gh2jqd.ea3mdgi5 {
            width: 100%;
            margin: 0 auto;
            max-width: 1200px;
        }
        .st-emotion-cache-1i41fkg.e1f1d6gn2{
            height: 600px;
            overflow-y: scroll; /* 添加垂直滚动条 */
        }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    selected_page = st.sidebar.radio(
        'Select Page which you want 👇',
        [":rainbow[首页]", ":green[novel助手]", ":blue[novel生成]",":red[设置]"],
        captions=["HomePage👻", "Novel Assistant😊", "Novel generation🤑","Settings😶"]
    )


    page_content(selected_page)