import os
import os.path
import json
from os import walk, makedirs, remove
import re
from codecs import open
from os.path import join, dirname, exists, relpath, abspath, basename, sep
from sys import platform
from json_tools import prepare, field_by_path, list_field_paths
from utils import get_answer
import requests
from patch_tool import trans_patch
if platform == "win32":
    from os.path import normpath as normpath_old


def sunlesssea_event_teaser(the_dir):
    print("events.json.json is loading")
    events_text = json.loads(
        prepare(open(the_dir, "rb+", "utf-8")))
    path_dict = dict()
    print("Loading complete")
    for i in events_text:
        if "Chs" in i["Texts"]:
            if i["Texts"]["Eng"] == i["Texts"]["Chs"]:
                del i["Texts"]["Chs"]
    for i in events_text:
        if "Chs" in i["Texts"]:
            w = i["Files"]
            for v in w["entities/events.json"]:
                if re.search(r".*/Description$", v):
                    path_dict[v.replace(
                        "/Description", "/Teaser")] = i["Texts"]["Chs"]
    for i in events_text:
        w = i["Files"]
        for v in w["entities/events.json"]:
            if re.search(r'.*Teaser$', v):
                if v in path_dict:
                    if re.search(r'! ', i["Texts"]["Eng"]):
                        Chs_text = path_dict[v].split('!')
                        i["Texts"]["Chs"] = Chs_text[0]+"! - "
                    elif re.search(r'\?', i["Texts"]["Eng"]):
                        Chs_text = path_dict[v].split('?')
                        i["Texts"]["Chs"] = Chs_text[0]+"?"
                    else:
                        Chs_text = path_dict[v].split('.')
                        i["Texts"]["Chs"] = Chs_text[0]+"..."
    f = open(the_dir, "wb+", "utf-8")
    f.write(json.dumps(
        events_text, ensure_ascii=False, sort_keys=True, indent=2))
    f.close


if __name__ == "__main__":
    sunlesssea_event_teaser(
        "F:/Sunless_Sea_Chinese_Translation_Mod_Re/translations/texts/entities/events.json.json",)
