"""
@FileName：novelGenerate.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/19 9:38
@Copyright：©2018-2024 awesome!
"""
import os

"""
负责生成，这里有非常多的操作，需要处理到
"""
import streamlit as st

class NovelGenerate:
    def __init__(self):
        # 在这里定义到我们的数据
        self.gen_data = {
            "novel_text":"",
            "temperature":0.4,
            "audio_select": "小艺",
            "language_select":"中文",
            "data":[{"提示词":"prompt1","分段":"part01",
                         "图片":None,"音频":None
                         },

                    {"提示词": "prompt1", "分段": "part01",
                     "图片": None, "音频": None
                     },
                    {"提示词": "prompt1", "分段": "part01",
                     "图片": None, "音频": None
                     },
                    {"提示词": "prompt1", "分段": "part01",
                     "图片": None, "音频": None
                     },   {"提示词": "prompt1", "分段": "part01",
                     "图片": None, "音频": None
                     },   {"提示词": "prompt1", "分段": "part01",
                     "图片": None, "音频": None
                     },

                        ]
        }
        if("gen_data" in st.session_state.keys()):
            self.gen_data = st.session_state.gen_data
        else:
            st.session_state.gen_data = self.gen_data

        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)

    def __down_lay_show(self,data_container,data):
        with data_container:
            show_popup = st.empty()
            with st.expander("view😃", expanded=True):
                st.write(data)
                if st.button("X"):
                    show_popup.empty()

    def __current_delete(self,index):
        print("删除-当前元素",index)


    def __current_gen(self,index):
        print("生成-当前元素",index)

    def page(self):
        col1,col2 = st.columns([1,2])
        with col1:
            novel_text = st.text_area(label="文本输入",placeholder="请输入小说文本🎈",height=400)
            temperature = st.slider("temperature",min_value=0.2,max_value=1.0,step=0.1,value=0.4)
            template = st.button("模板生成",type="primary")
        with col2:
            st.markdown("当前版本直接生成视频，后续增加对简映模板的支持ヾ(≧▽≦*)o")
            c1,c2,c3,c4,c5,c6 = st.columns(6)
            with c1:
                batch_gen = st.button("批量生成",type="primary")
            with c2:
                export_button_jianying = st.button("导出简映",type="primary")
            with c3:
                export_button_video = st.button("导出视频",type="primary")
            with c4:
                audio_select = st.selectbox("音频选择",("小艺","云建","云溪","云霞","云阳","小北","小妮"))
            with c5:
                language_select = st.selectbox("语言选择",("中文","英文"))
            with c6:
                add_button  = st.button("添加",type="primary")
            # 展示数据的容器
            st.markdown("----------------->生成内容👻🦅👇")
            data_container = st.container(height=400)
            data = self.gen_data.get("data")
            for index in range(len(data)):
                with data_container:
                    # 创建一行多列的布局
                    c01, c02, c03, c04, c05, c06,c07 = st.columns([2, 2, 1, 1, 1, 1,1])
                    current_line_data = data[index]
                    with c01:
                        # 加载图片
                        default_img = self.current_dir+r"/../../assert/img/bg.jpg"
                        if(current_line_data["图片"] != None):
                            st.image(current_line_data["图片"] ,caption="生成")
                        else:
                            st.image(default_img,  caption="示例")
                    with c02:
                        # 加载音频
                        default_audio = self.current_dir + r"\..\..\assert\audio\test01.mp3"
                        if (current_line_data["音频"] != None):
                            st.text("生成")
                            st.audio(current_line_data["音频"])
                        else:
                            st.text("示例")
                            st.audio(default_audio)

                    with c03:
                        if st.button("提示"+str(index)):
                            self.__down_lay_show(data_container, current_line_data.get("提示词", ""))

                    with c04:
                        if st.button("分段" + str(index)):
                            with data_container:
                                self.__down_lay_show(data_container,current_line_data.get("分段", ""))

                    with c05:
                        st.selectbox("音频" + str(index),
                                     ("小艺", "云建", "云溪", "云霞", "云阳", "小北", "小妮"))

                    with c06:
                        if st.button("删除"+str(index)):
                            self.__current_delete(index)

                    with c07:
                        if st.button("生成"+str(index),type="primary"):
                            self.__current_gen(index)








