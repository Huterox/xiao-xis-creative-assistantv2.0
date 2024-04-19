"""
@FileName：novelGenerate.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/19 9:38
@Copyright：©2018-2024 awesome!
"""
import os
import time

from handler.storyboardHandler import StoryBoardHandler

"""
负责生成，这里有非常多的操作，需要处理到
"""
import streamlit as st
from streamlit_modal import Modal
modal = Modal(key="Data",title="view😀")
class NovelGenerate:
    def __init__(self):
        # 在这里定义到我们的数据
        self.gen_data = {
            "novel_text":"",
            "temperature":0.5,
            "audio_select": "小艺",
            "language_select":"中文",
            "data":[
                    {
                        "提示词":"prompt1",
                        "分段":"part01",
                        "图片":None,
                        "音频":None
                    },
                    ]
        }

        if("gen_data" in st.session_state.keys()):
            self.gen_data = st.session_state.gen_data
        else:
            st.session_state.gen_data = self.gen_data

        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)
        self.storyBoardHandler = StoryBoardHandler()

    # 保证我们当前的gen_data和在session里面的是一致的
    def __get_gen_data(self):
        if ("gen_data" in st.session_state.keys()):
            self.gen_data = st.session_state.gen_data
        else:
            st.session_state.gen_data = self.gen_data
        return self.gen_data

    # 刷新机制的问题，该方案无法使用
    @Warning
    def __down_lay_show(self,data_container,data,index,key):
        with data_container:
            with st.expander("view😃", expanded=True):
                current_line_data = data.get("data")[index]
                pro = st.text_input(label="内容", value=current_line_data.get(key, ""))
                if pro:
                    # print("pro", pro)
                    current_line_data[key] = pro
                    # print(current_line_data, "-----current_line")
                    data['data'][index] = current_line_data
                    st.session_state.gen_data = data
                    self.gen_data = data

    def __current_delete(self,index):
        print("删除-当前元素",index)


    def __current_gen(self,index):
        print("生成-当前元素",index)

    def __gen_model_fn(self):

        # 做一些防抖
        if("__gen_model_fn" is not st.session_state.keys()):
            # 首次访问方法
            st.session_state.__gen_model_fn = True
        else:
            if (st.session_state.__gen_model_fn == True):
                with modal.container():
                    st.success("当前任务执行中，请勿重复提交...😯")
                    return
        st.session_state.__gen_model_fn = True
        # 在这里生成模板，生成的话只需要将结果存放到data当中即可，然后会自动刷新
        novel_text = self.novel_text
        temperature = self.temperature
        # 如果这两个参数没有发生改变，那么我们不执行
        gen_data = self.__get_gen_data()
        try:
            if gen_data and gen_data.get("temperature") == temperature and gen_data.get("novel_text") == novel_text:
                with self.b_c1:
                    with st.spinner("努力工作中，请勿操作😁"):
                        time.sleep(1)
                with modal.container():
                    st.success("执行完毕！😎")
                st.session_state.__gen_model_fn = False
            else:
                # 先更新这两个参数，再执行方法
                self.gen_data["temperature"] = temperature
                self.gen_data["novel_text"] = novel_text
                # 再更新到session
                st.session_state.gen_data = self.gen_data
                # 开始执行到我们的方法
                with self.b_c1:
                    with st.spinner("努力工作中，请勿操作😁"):
                        data_list = self.storyBoardHandler.getProgressHandler(novel_text,temperature)
                        # 拿到data,我们按照格式，先更新上gen_data里面的data当中就ok了
                        data:list[dict] = []
                        index = 1
                        for line_dict in data_list:
                            temp = {"提示词": line_dict.get("描述" + str(index)),
                                    "分段": line_dict.get("场景" + str(index)),
                                    "图片": None,
                                    "音频": None}
                            data.append(temp)
                            index += 1
                        # 再将data更新上去
                        self.gen_data["data"] = data
                        st.session_state.gen_data = self.gen_data
                st.session_state.__gen_model_fn = False
                with modal.container():
                    st.success("执行完毕！😎")
        except Exception as e:
            with modal.container():
                st.success("当前网络异常，请稍后重试！😫")
        finally:
            st.session_state.gen_data = self.gen_data
            st.session_state.__gen_model_fn = False

    def page(self):
        col1,col2 = st.columns([1,2])
        with col1:
            gen_data = self.__get_gen_data()
            self.novel_text = st.text_area(label="文本输入",placeholder="请输入小说文本🎈",
                                           height=380,value=gen_data.get("novel_text"))
            self.temperature = st.slider("temperature",min_value=0.2,max_value=1.0,step=0.1,
                                         value=gen_data.get("temperature"),)
            self.b_c0,self.b_c1 = st.columns([1,2])
            with self.b_c0:
                self.template = st.button("模板生成",type="primary")
            if(self.template):
                self.__gen_model_fn()
        with col2:
            st.markdown("当前版本直接生成视频，后续增加对简映模板的支持ヾ(≧▽≦*)o")
            c1,c2,c3,c4,c5,c6 = st.columns(6)
            with c1:
                self.batch_gen = st.button("批量生成",type="primary")
            with c2:
                self.export_button_jianying = st.button("导出简映",type="primary")
            with c3:
                self.export_button_video = st.button("导出视频",type="primary")
            with c4:
                self.audio_select = st.selectbox("音频选择",("小艺","云建","云溪","云霞","云阳","小北","小妮"))
            with c5:
                self.language_select = st.selectbox("语言选择",("中文","英文"))
            with c6:
                self.add_button  = st.button("添加",type="primary")
            # 展示数据的容器
            st.markdown("----------------->生成内容👻🦅👇")
            data_container = st.container(height=400)
            data = self.gen_data
            for index in range(len(data.get("data"))):
                with data_container:
                    # 创建一行多列的布局,现在拿到当前行的数据
                    c01, c02, c03, c04, c05, c06,c07 = st.columns([4, 3, 2, 2, 2, 2,2])
                    current_line_data = data.get("data")[index]
                    with c01:
                        # 加载图片
                        default_img = self.current_dir+r"/../../assert/img/wait.jpg"
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
                            with col2:
                                with modal.container():
                                    if pro:=st.text_area(
                                                 label="提示词-暂不支持修改"+str(index),
                                                 value=current_line_data["提示词"],
                                                 height=200
                                                 ):
                                        print("pro:",pro)

                            # self.__down_lay_show(data_container,data,index,"提示词")
                        # st.text_area(height=50,value=current_line_data["提示词"],label="提示词"+str(index))

                    with c04:
                        if st.button("分段" + str(index)):
                            with col2:
                                with modal.container():
                                    if pro := st.text_area(
                                            label="分段-暂不支持修改" + str(index),
                                            value=current_line_data["分段"],
                                            height=200
                                    ):
                                        print("pro:",pro)
                            # self.__down_lay_show(data_container,data,index,"分段")
                        # st.text_area(height=50, value=current_line_data["分段"], label="分段"+str(index))

                    with c05:
                        st.selectbox("音频" + str(index),
                                     ("小艺", "云建", "云溪", "云霞", "云阳", "小北", "小妮"))

                    with c06:
                        if st.button("删除"+str(index)):
                            self.__current_delete(index)

                    with c07:
                        if st.button("生成"+str(index),type="primary"):
                            self.__current_gen(index)








