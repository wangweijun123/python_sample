# -*- coding: cp936 -*-
import os

def rename_files():
    print("call rename method")
    # ��һ����ȡ�ļ��б�
    file_list = os.listdir(r"E:\study\udacity\python\entry_door\test")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"E:\study\udacity\python\entry_door\test")
    # �ڶ��� �޸��ļ���
    for file_name in file_list:
        print("file_name:"+file_name)
        print(file_name.translate(None, "0123456"))
        os.rename(file_name, file_name.translate(None, "0123456"))


# ע��ո�python �Ŀո�,�����ĵ���ǰ�治���пո�
rename_files()
