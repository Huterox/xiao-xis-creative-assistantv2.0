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
from app.text2video.webui.main import  run_app_text2videoApp


def index():

    st.markdown("*Novel-Video创作助手* is **really** ***cool*** --v0.1beta（￣︶￣）↗　.")
    st.markdown('''
        :red[自带] :orange[小汐] :green[创作助手] :blue[完成文档润色] :violet[流水线]
        :gray[内容生成] :rainbow[解放双手].
        :yellow[v2.x版本支持集成其他模块] 
        当前集成第三方模块，文本生成视频：[https://github.com/harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
        
        ''')
    st.markdown("Welcome to here! &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    st.image(current_dir+r"/assert/img/bg.jpg",width=800)



st.set_page_config(page_title="小汐创作助手",
                   page_icon="🤖",
                   layout="wide",
                   initial_sidebar_state="auto",
              )


if __name__ == "__main__":
    def page_content(page):
        if page == ':rainbow[首页]':
            index()
        if page == ':green[novel创作]':
            run_app_novel()
        elif page == ':blue[文本生视频]':
            run_app_text2videoApp()
        elif page == ':red[YouTube搬运]':
            st.write(":red[YouTube搬运]")


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
        [":rainbow[首页]", ":green[novel创作]", ":blue[文本生视频]", ":red[YouTube搬运]"],
        captions=["HomePage👻", "Novel Assistant😊", "文本生视频🤑", "YouTube😶"]
    )

    page_content(selected_page)