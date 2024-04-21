"""
@FileName：novelGenerate.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/19 9:38
@Copyright：©2018-2024 awesome!
"""

import os
import time
from PIL import Image
from handler.storyboardHandler import StoryBoardHandler
import concurrent.futures

from handler.videoBuilder import VideoBuilder

"""
负责生成，这里有非常多的操作，需要处理到
"""
import streamlit as st
from streamlit_modal import Modal
modal = Modal(key="Data",title="view😀")
class NovelGenerate:
    def __init__(self):
        # 在这里定义到我们的数据

        self.current_file_path = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file_path)
        self.storyBoardHandler = StoryBoardHandler()
        self.default_img = self.current_dir+r"/../../assert/img/wait.jpg"
        self.default_audio = self.current_dir + r"\..\..\assert\audio\test01.mp3"
        self.video_builder = VideoBuilder()

        self.gen_data = {
            "novel_text":"",
            "temperature":0.4,
            "audio_select": "小艺",
            "language_select":"中文",
            "data":[
                    {
                        "提示词":"prompt0",
                        "分段":"part0",
                        "图片":self.default_img,
                        "音频":self.default_audio
                    },
                    {
                        "提示词": "prompt1",
                        "分段": "part1",
                        "图片": self.default_img,
                        "音频": self.default_audio
                    },
                    ]
        }

        if("gen_data" in st.session_state.keys()):
            self.gen_data = st.session_state.gen_data
        else:
            st.session_state.gen_data = self.gen_data

    def __export_video_fn(self):
        gen_data = self.__get_gen_data()
        data = gen_data.get("data")
        with self.data_container:
            with st.spinner("正在导出视频...请勿进行其他操作(＾Ｕ＾)ノ~ＹＯ"):
                save_path = self.video_builder.data2Video(data)
                if(save_path!=-1):
                    with self.col2:
                        with modal.container():
                            # 读取MP4文件的内容
                            with open(save_path, 'rb') as file:
                                mp4_content = file.read()
                            st.success("导出成功！")
                            # 创建一个下载按钮，允许用户下载MP4文件
                            st.download_button(label="下载视频", data=mp4_content, file_name='video.mp4',
                                               mime='video/mp4')
                else:
                    st.error("哦┗|｀O′|┛ 嗷~~，好像出现为止错误😫")


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
        # print("删除-当前元素",index)
        gen_data = self.__get_gen_data()
        data_list:list = gen_data.get("data")
        data_list.pop(index)
        st.session_state.gen_data = gen_data
        # 为了保证能够立马刷新，只能加一个弹窗，这是由于StreamLit的执行机制决定的
        with self.col2:
            with modal.container():
                st.success("执行完毕")

    def __current_add(self):
        gen_data = self.__get_gen_data()
        data_list: list = gen_data.get("data")
        index = len(data_list)
        data_list.append(
            {
                "提示词": "prompt"+str(index),
                "分段": "part"+str(index),
                "图片": None,
                "音频": None
            },
        )
        st.session_state.gen_data = gen_data
        # 为了保证能够立马刷新，只能加一个弹窗，这是由于StreamLit的执行机制决定的
        with self.col2:
            with modal.container():
                st.success("执行完毕")

    def __batch_gen_fn(self):
        gen_data = self.__get_gen_data()
        data_list: list = gen_data.get("data")
        data_list_len = len(data_list)
        task = []
        condition = []
        with self.col2:
            with st.spinner("生成中..."):
                with concurrent.futures.ThreadPoolExecutor(max_workers=min(data_list_len, 4)) as executor:  # 限制最大线程数
                    futures = [executor.submit(self.__current_gen_batch, index, condition) for index in
                               range(data_list_len)]
                    condition = []
                    for future in concurrent.futures.as_completed(futures):
                        future.result()
                # 执行完毕给提示
                with self.col2:
                    with modal.container():
                        if(len(condition)==0):
                            st.success("执行完毕")
                        else:
                            info = "部分任务执行失败{"
                            for i in condition:
                                info+=str(i)+","
                            info+="}"
                            st.warning(info)


    def __current_gen_batch(self,index,condition:list):

        # 这里主要生成画面和音频
        gen_data = self.__get_gen_data()
        current_line_data = gen_data.get("data")[index]
        prompt = current_line_data.get("提示词")
        part_text = current_line_data.get("分段")
        audio_select = gen_data.get("audio_select")
        language_select = gen_data.get("language_select")
        args_for_getText2Img = (prompt,)
        args_for_getText2Audio = (part_text,audio_select,language_select,)
        # 默认任务得到的结果
        result = {
            "audio": -1,
            "image": -1
        }
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                future_to_task = {
                }
                # 生成图片
                future_img= executor.submit(self.storyBoardHandler.getText2Img, *args_for_getText2Img)
                future_to_task[future_img] = "image"
                # 生成语音
                future_audio = executor.submit(self.storyBoardHandler.getText2Audio, *args_for_getText2Audio)
                future_to_task[future_audio] = "audio"
                for future in concurrent.futures.as_completed(future_to_task):
                    result[future_to_task.get(future)] = future.result()
                    if(future_to_task.get(future)=="image"):
                        current_line_data["图片"] = result.get("image")
                    else:
                        current_line_data["音频"] = result.get("audio")

            st.session_state.gen_data = self.gen_data
            with self.col2:
                with modal.container():
                    st.success("执行完毕")
        except Exception as e:
            # 当前这个index任务执行失败
            condition.append(index)
            print(e)
            return -1
        return 1

    def __current_gen(self,index):

        st.session_state["__current_gen_button"+str(index)] = True
        # 这里主要生成画面和音频
        gen_data = self.__get_gen_data()
        current_line_data = gen_data.get("data")[index]
        prompt = current_line_data.get("提示词")
        part_text = current_line_data.get("分段")
        audio_select = gen_data.get("audio_select")
        language_select = gen_data.get("language_select")
        args_for_getText2Img = (prompt,)
        args_for_getText2Audio = (part_text,audio_select,language_select,)
        # 默认任务得到的结果
        result = {
            "audio": -1,
            "image": -1
        }
        try:
            with self.data_container:
                with st.spinner("生成中，注意只允许同时执行一个任务😐，重复提交，或执行其他任务将导致其他任务取消..."):
                    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                        future_to_task = {
                        }
                        # 生成图片
                        future_img= executor.submit(self.storyBoardHandler.getText2Img, *args_for_getText2Img)
                        future_to_task[future_img] = "image"
                        # 生成语音
                        future_audio = executor.submit(self.storyBoardHandler.getText2Audio, *args_for_getText2Audio)
                        future_to_task[future_audio] = "audio"
                        for future in concurrent.futures.as_completed(future_to_task):
                            result[future_to_task.get(future)] = future.result()
                            if(future_to_task.get(future)=="image"):
                                current_line_data["图片"] = result.get("image")
                            else:
                                current_line_data["音频"] = result.get("audio")

                    st.session_state.gen_data = self.gen_data
                    with self.col2:
                        with modal.container():
                            st.success("执行完毕")
        except Exception as e:
            with self.col2:
                with modal.container():
                    st.error("哦┗|｀O′|┛ 嗷~~，发生了不可名状的异常(⊙o⊙)？")
            print(e)


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
        self.col1,self.col2 = st.columns([1,2])
        with self.col1:
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
        with self.col2:
            st.markdown("当前版本直接生成视频，后续增加对简映模板的支持ヾ(≧▽≦*)o")
            c1,c2,c3,c4,c5,c6 = st.columns(6)
            with c1:
                self.batch_gen = st.button("批量生成",type="primary",on_click=self.__batch_gen_fn)
            with c2:
                self.export_button_jianying = st.button("导出剪映",type="primary")
            with c3:
                self.export_button_video = st.button("导出视频",type="primary",on_click=self.__export_video_fn)
            with c4:
                self.audio_select = st.selectbox("音频选择",("小艺","云建","云溪","云霞","云阳","小北","小妮"))
                if self.audio_select:
                    self.gen_data["audio_select"] = self.audio_select
                    st.session_state.gen_data = self.gen_data
            with c5:
                self.language_select = st.selectbox("语言选择",("中文","英文"))
                if self.language_select:
                    self.gen_data["language_select"] = self.language_select
                    st.session_state.gen_data = self.gen_data
            with c6:
                self.add_button  = st.button("添加",type="primary",on_click=self.__current_add)
            # 展示数据的容器
            st.markdown("----------------->生成内容👻🦅👇")
            self.data_container = st.container(height=400)
            data = self.gen_data
            for index in range(len(data.get("data"))):
                with self.data_container:
                    # 创建一行多列的布局,现在拿到当前行的数据
                    c01, c02, c03, c04,c06,c07 = st.columns([4, 3, 2, 2, 2,2])
                    current_line_data = data.get("data")[index]
                    with c01:
                        # 加载图片
                        if(current_line_data["图片"] != self.default_img):
                            if(current_line_data["图片"]!=-1):
                                st.image(current_line_data["图片"] ,caption="生成-成功",)
                            else:
                                image = Image.open(self.default_img)
                                st.image(image, caption="生成-失败")
                        else:
                            image = Image.open(self.default_img)
                            st.image(image,  caption="示例")
                    with c02:
                        # 加载音频

                        if (current_line_data["音频"] != self.default_audio):
                            if(current_line_data["音频"]!=-1):
                                st.text("生成-成功")
                                st.audio(current_line_data["音频"])
                            else:
                                st.text("生成-失败")
                                st.audio(self.default_audio)
                        else:
                            st.text("示例")
                            st.audio(self.default_audio)

                    with c03:
                        # 查看文本-提示词
                        st.button("提示"+str(index),on_click=self.c03_button_click,args=(index,current_line_data,))

                    with c04:
                        # 查看文本-分段
                        st.button("分段" + str(index), on_click=self.c04_button_click,args=(index,current_line_data,))

                    # with c05:
                    #     st.selectbox("音频" + str(index),
                    #                  ("小艺", "云建", "云溪", "云霞", "云阳", "小北", "小妮"))

                    with c06:
                        if st.button("删除"+str(index)):
                            self.__current_delete(index)

                    with c07:
                        if st.button("生成"+str(index),type="primary"):
                            self.__current_gen(index)

    def c03_button_click(self,index,current_line_data):
        with self.col2:
            with modal.container():
                prop_text_key = "view_prompt_key" + str(index)
                pro = st.text_area(
                    label="生成图像提示词" + str(index),
                    value=current_line_data["提示词"],
                    height=150,
                    key=prop_text_key
                )

                def show_pro():
                    new_prompt_text = st.session_state.get(prop_text_key)
                    current_line_data["提示词"] = new_prompt_text
                    # 将这个修改之后的数据保存到session当中去
                    st.session_state.gen_data = self.gen_data

                st.button("保存提示词" + str(index), on_click=show_pro)

    def c04_button_click(self,index,current_line_data):
        with self.col2:
            with modal.container():
                part_text_key = "view_part_key" + str(index)
                part = st.text_area(
                    label="划分分段" + str(index),
                    value=current_line_data["分段"],
                    height=150,
                    key=part_text_key
                )

                def show_pro():
                    new_part_text = st.session_state.get(part_text_key)
                    current_line_data["分段"] = new_part_text
                    # 将这个修改之后的数据保存到session当中去
                    st.session_state.gen_data = self.gen_data
                st.button("保存分段" + str(index), on_click=show_pro)

