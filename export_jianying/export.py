"""
@FileName：export.py
@Author：Huterox
@Description：Go For It
@Time：2024/4/17 0:49
@Copyright：©2018-2024 awesome!
"""
import json

# 定义草稿内容的基本结构
def create_draft_content():
    draft_content = {
        "version": "1.0.0",
        "canvases": [],
        "material_animations": [],
        "speeds": [],
        "texts": [],
        "video_tracks": [],
        "audio_tracks": []
    }
    return draft_content

# 定义草稿元信息的基本结构
def create_draft_meta_info(title, author, description):
    draft_meta_info = {
        "title": title,
        "author": author,
        "description": description,
        "created_time": "2024-04-17T12:00:00",
        "modified_time": "2024-04-17T12:00:00"
    }
    return draft_meta_info

# 保存草稿内容和元信息到文件
def save_draft_files(draft_content, draft_meta_info, content_file_path, meta_file_path):
    with open(content_file_path, 'w', encoding='utf-8') as f:
        json.dump(draft_content, f, ensure_ascii=False, indent=4)

    with open(meta_file_path, 'w', encoding='utf-8') as f:
        json.dump(draft_meta_info, f, ensure_ascii=False, indent=4)

# 主函数，创建并保存草稿文件
def main():
    draft_title = "我的剪映项目"
    draft_author = "用户"
    draft_description = "这是一个由Python脚本生成的剪映项目模板"

    # 创建草稿内容和元信息
    draft_content = create_draft_content()
    draft_meta_info = create_draft_meta_info(draft_title, draft_author, draft_description)

    # 保存到文件
    content_file_path = "draft_content.json"
    meta_file_path = "draft_meta_info.json"
    save_draft_files(draft_content, draft_meta_info, content_file_path, meta_file_path)

    print("剪映项目模板文件已生成。")

if __name__ == "__main__":
    main()