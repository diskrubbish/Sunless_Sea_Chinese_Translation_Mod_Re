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


def step_1(json,key):
    dict_1 = list()
    for i in json:
        if key in i and i[key] is not None:
            cache_1 = list()
            cache_1.append(i["Id"])
            cache_1.append(i[key])
            dict_1.append(cache_1)
            """
                if "RareDefaultEvent" in v and v["RareDefaultEvent"] is not None:
                    w = v["RareDefaultEvent"]
                    if "Teaser" in w and w["Teaser"] is not None:
                        cache_1 = list()
                        cache_1.append(w["Id"])
                        cache_1.append(w["Teaser"])
                    ##print (w["Description"])
                    # dict_1.append(zip(w["Description"],w["Id"]))
                        dict_1.append(cache_1)
            """
    return(dict_1)


if __name__ == "__main__":    
    target = json.loads(prepare(open(
        "F:/Sunless_Sea_Chinese_Translation_Mod_Re/translations/texts/entities/qualities.json.json", "r", "utf-8-sig")))
    old = json.loads(prepare(
        open("F:/Sunless_Sea_Data/cn_translation/entities/qualities.json", "r", "utf-8-sig")))
    new = json.loads(prepare(
        open("F:/Sunless_Sea_Data/Sunless Sea_source_file/entities/qualities.json", "r", "utf-8-sig")))
    old_data = step_1(old,"ChangeDescriptionText")
    new_data = step_1(new,"ChangeDescriptionText")
    dict_2 = dict()
    for i in old_data:
        for v in new_data:
            if i[0] == v[0]:
                dict_2[v[1]] = i[1]
    
    for w in target:
        if "Chs"  in w["Texts"]:
            pass
        else:
            if w["Texts"]["Eng"] in dict_2:
                w["Texts"]["Chs"] = dict_2[w["Texts"]["Eng"]]
        ##if  w["Texts"]["Chs"] in w["Texts"] and w["Texts"]["Chs"] == w["Texts"]["Eng"]:
        ##    del w ["Texts"]["Chs"]
        ##if  w["Texts"]["Chs"] in w["Texts"] and w["Texts"]["Chs"] == w["Texts"]["Eng"]:
        ##    del w ["Texts"]["Chs"]
    f = open(
        "F:/Sunless_Sea_Chinese_Translation_Mod_Re/translations/texts/entities/qualities.json.json", "wb+", "utf-8")
    f.write(json.dumps(target, ensure_ascii=False, sort_keys=True, indent=2))
    f.close
