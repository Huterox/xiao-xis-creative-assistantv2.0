"""
@FileName：app.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/21 23:56
@Copyright：©2018-2024 awesome!
"""
import json
import os
import time

from plugings.export_jianying.utils.beate import tracks
from plugings.export_jianying.utils.util import *

"""
ExportApp 保持单例模式 --v0.2.5 暂时放弃该方案   
                        导出模板修改为，导出素材，便于用户在不同的软件中使用
"""
class ExportApp(object):

    def __init__(self,base_path,folder_path,
                 template_meta_info_path,
                 template_meta_content_path):
        """
        :param base_path: 模板生成器基本工作目录
        :param folder_path: 模板对应文件夹
        :param novel_name: 对应生成的模板名字
        :param template_meta_info_path: 媒体信息文件
        :param template_meta_content_path: 媒体排布文件
        """
        self.base_path = base_path
        self.folder_path = folder_path
        self.template_meta_info_path = template_meta_info_path
        self.template_meta_content_path = template_meta_content_path



    def init_data(self,novel_name):
        """
        初始化数据
        """
        # 读取模板
        self.draft_content_template = read_json(self.template_meta_content_path)
        self.draft_meta_template = read_json(self.template_meta_info_path)

        self.draft_content_template['id'] = generate_id()  # 给模版ID设置唯一id
        tracks_video_data = tracks()  # 创建tracks用于存放图片信息
        tracks_video_data['type'] = 'video'  # 类型
        self.draft_content_template['tracks'].append(tracks_video_data)  # 添加到模板里

        tracks_audio_data = tracks()  # 创建tracks用于存放音频信息
        tracks_audio_data['type'] = 'audio'  # 类型
        self.draft_content_template['tracks'].append(tracks_audio_data)  # 添加到模板里

        self.draft_meta_template['draft_id'] = generate_id()  # 给模版ID设置唯一id
        self.draft_meta_template[
            'draft_root_path'] = self.base_path
            # 剪映的草稿路劲 如：D:\\\\software\\\\剪映\\\\JianyingPro Drafts
        self.draft_meta_template['tm_draft_create'] = int(time.time() * 1000)
        # draft_meta_info.json创建时间，时间戳
        self.draft_meta_template['tm_draft_modified'] = generate_16_digit_timestamp()
        # 13或16位毫秒级时间戳generate_16_digit_timestamp()
        self.draft_meta_template['draft_removable_storage_device'] = get_drive_from_path(self.base_path)
        # 磁盘的驱动器 如"D:"
        self.draft_meta_template['draft_fold_path'] = self.folder_path.replace('\\',
                                                                               '/')
        # 剪映安装路劲加上草稿名字 如： D:/software/剪映/JianyingPro Drafts/六合八荒唯我独尊
        self.draft_meta_template['draft_name'] = novel_name
        # 草稿名字 如："D:/software/剪映/JianyingPro Drafts/六合八荒唯我独尊"

    def write_data(self,meta_info_path,content_path):
        """
        创建文件,并写入数据
        """
        # 创建文件夹
        os.makedirs(self.folder_path, exist_ok=True)
        # 创建 draft_meta_info.json
        with open(meta_info_path, 'w', encoding='utf-8') as meta_info_file:
            json.dump(self.draft_meta_template, meta_info_file, indent=4, ensure_ascii=False)

        with open(content_path, 'w', encoding='utf-8') as content_file:
            json.dump(self.draft_content_template, content_file, indent=4, ensure_ascii=False)

