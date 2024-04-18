"""
@FileName：novelAssistant.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/18 21:14
@Copyright：©2018-2024 awesome!
"""
import time

import streamlit as st

from handler.helperChat import ChatBotHandler


class AssistantNovel(object):

    def __init__(self):
        self.chat = ChatBotHandler()

    def get_response(self,prompt, history):
        return self.chat.signChat(history)

    def clear_chat_history(self):
        st.session_state.messages = [{"role": "assistant", "content": "🍭🍡你好！我是全能创作助手~小汐🥰，可以帮助您完善补充文案细节？🧐"}]

    def page(self):
        # 主聊天对话窗口
        prompt = st.chat_input(placeholder="请输入对话")

        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "🍭🍡你好！我是全能创作助手~小汐🥰，可以帮助您完善补充文案细节？🧐"}]

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = self.get_response(prompt,st.session_state.messages)
                    placeholder = st.empty()
                    full_response = ''
                    for item in response:
                        full_response += item
                        time.sleep(0.01)
                        placeholder.markdown(full_response)
                    placeholder.markdown(full_response)
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)
        st.button('清空历史对话', on_click=self.clear_chat_history)