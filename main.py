"""
@Author：Huterox
@Description：Go For It
@Time：2024/4/16 8:58
@Copyright：©2018-2024 awesome!
"""

from utils import getConfig
from webui.streamlit.novelAssistant import AssistantNovel

config = getConfig()
import streamlit as st

def index():

    st.markdown("*Novel-Video创作助手* is **really** ***cool*** --v0.1beta（￣︶￣）↗　.")
    st.markdown('''
        :red[自带] :orange[小汐] :green[创作助手] :blue[完成文档润色] :violet[流水线]
        :gray[内容生成] :rainbow[解放双手].''')
    st.markdown("Welcome to here! &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


if __name__ == '__main__':

    def page_content(page):
        if page == ':rainbow[首页]':
            index()
        if page == ':green[novel助手]':
            assistant = AssistantNovel()
            assistant.page()
        elif page == ':blue[novel生成]':
            st.title('这是页面 2')
            st.write('页面 2 的内容。')
        elif page == ':red[设置]':
            st.title('这是页面 3')
            st.write('页面 3 的内容。')


    selected_page = st.sidebar.radio(
        'Select Page which you want 👇',
        [":rainbow[首页]", ":green[novel助手]", ":blue[novel生成]",":red[设置]"],
        captions=["HomePage👻", "Novel Assistant😊", "Novel generation🤑","Settings😶"]
    )


    page_content(selected_page)