
import os

def batch_rename_files(folder_path, suffix):
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]

    for file_path in file_paths:
        if os.path.isfile(file_path):
            file_name, file_ext = os.path.splitext(file_path)
            new_file_name = file_name + suffix + file_ext

            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(file_path, new_file_path)

# 用法示例
folder_path = '/Potsdam/SegmentationClass'  # 文件夹路径
suffix = '_lab'

batch_rename_files(folder_path, suffix)
