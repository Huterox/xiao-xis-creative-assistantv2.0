"""
@FileName：main.py.py
@Author：Huterox
@Description：Go For It
@Time：2024/5/2 10:59
@Copyright：©2018-2024 awesome!
"""

import streamlit as st
import os
from app.novelMaker.main import run_app_novel

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


if __name__ == "__main__":
    def page_content(page):
        if page == ':rainbow[首页]':
            index()
        if page == ':green[novel创作]':
            run_app_novel()
        elif page == ':blue[文本生视频]':
            st.write(":blue[文本生视频]")
        elif page == ':red[YouTube搬运]':
            st.write(":red[YouTube搬运]")


    selected_page = st.sidebar.radio(
        'Select Page which you want 👇',
        [":rainbow[首页]", ":green[novel创作]", ":blue[文本生视频]", ":red[YouTube搬运]"],
        captions=["HomePage👻", "Novel Assistant😊", "文本生视频🤑", "YouTube😶"]
    )

    page_content(selected_page)