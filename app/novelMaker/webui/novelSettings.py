"""
@FileName：novelSettings.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/19 8:40
@Copyright：©2018-2024 awesome!
"""
import streamlit as st

import os

from app.novelMaker.utils import Config

"""
负责处理系统设置，当前设置单次有效，因为要支持多用户使用
"""

class NovelSettings(object):

    def __init__(self):
        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)

    def __temp_save_config(self,openai_key,base_url,default_model,mj_api_key,global_temperature):
        Config.settings["openai_api_key"] = openai_key
        Config.settings["openai_api_base"] = base_url
        Config.settings["default_model"] = default_model
        Config.settings["image_api_key"] = mj_api_key
        Config.settings["temperature"] = global_temperature
        st.session_state.settings = Config.settings

    def page(self):
        # 左侧边栏还是设置，右侧还是音频展示
        col1,col2 = st.columns([1, 2])
        gap = "50px"
        # 为列之间的间隔添加CSS样式
        st.markdown(f"<style>.streamlit-column{{ padding-right: {gap}; }}</style>", unsafe_allow_html=True)
        with col1:

            st.markdown('''
                :red[设置仅当前有效哟😎],\n
                :green[刷新后恢复默认设置😝]''')
            # 创建文本输入框
            openai_key = st.text_input("请输入你的OpenAI key", value=Config.settings.get("openai_api_key"))
            base_url = st.text_input("请输入你的Base Url", value=Config.settings.get("openai_api_base"))
            default_model = st.text_input("请输入你的Default Model", value=Config.settings.get("default_model"))
            mj_api_key = st.text_input("请输入你的绘画API Key", value=Config.settings.get("image_api_key"))
            # 创建数字输入框
            global_temperature = st.number_input("设置全局temperature", min_value=0.1, max_value=1.0, step=0.1,
                                                 value=Config.settings.get("temperature"))
            save_button = st.button("保存设置")
            # 这里可以根据需要添加保存设置的逻辑
            if save_button:
                self.__temp_save_config(openai_key, base_url, default_model, mj_api_key, global_temperature)
                show_popup = st.empty()
                with st.expander("提示🍡", expanded=True):
                    st.write(":green[nice，仅当前有效哟~😊。]")
                    # 添加一个按钮来关闭弹窗
                    if st.button("关闭"):
                        show_popup.empty()
        with col2:
            st.markdown('''
                 :blue[语音试听🍳]''')

            c01,c02,c03 = st.columns(3)
            with c01:
                st.text("小艺")
                st.audio(self.current_dir+r"\..\..\novelMaker\assert\audio\test01.mp3")
                st.text("云建")
                st.audio(self.current_dir+r"\..\..\novelMaker\assert\audio\test02.mp3")
                st.text("云溪")
                st.audio(self.current_dir + r"\..\..\novelMaker\assert\audio\test03.mp3")
            with c02:
                st.text("云霞")
                st.audio(self.current_dir+r"\..\..\novelMaker\assert\audio\test04.mp3")
                st.text("云阳")
                st.audio(self.current_dir + r"\..\..\novelMaker\assert\audio\test05.mp3")
                st.text("小北")
                st.audio(self.current_dir + r"\..\..\novelMaker\assert\audio\test06.mp3")
            with c03:
                st.text("小妮")
                st.audio(self.current_dir+r"\..\..\novelMaker\assert\audio\test07.mp3")
