import os
import os.path
import json
from os import walk, makedirs, remove
import re
from codecs import open
from os.path import join, dirname, exists, relpath, abspath, basename
from sys import platform
from json_tools import prepare, field_by_path, list_field_paths
from utils import get_answer
import requests
from patch_tool import trans_patch
if platform == "win32":
    from os.path import normpath as normpath_old


def tanslation(old, new):
    jsondata = json.loads(prepare(new))
    old_data = json.loads(prepare(old))
    for i in old_data:
        list_1 = list(i['Files'].values())
        for v in jsondata:
            for w in list(v['Files'].values()):
                if w in list_1:
                    v['Texts']['Chs'] = i['Texts']['Eng']
    result = json.dumps(jsondata, ensure_ascii=False,
                        sort_keys=True, indent=2)
    return result


if __name__ == "__main__":
    print("该脚本可以将patch文件的老文本导入指定json文件，")
    old = input("现在，请输入patch文件路径：").replace("\\", "/")
    new = input("现在, 请输入json文件夹路径：").replace("\\", "/")
    text = tanslation(open(old, "r", "utf-8"), open(new, "r", "utf-8"))
    f = open(new, "wb+", "utf-8")
    f.write(text)
    f.close
    print("处理完毕。")
