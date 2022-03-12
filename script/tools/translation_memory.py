import json
from os import walk, makedirs, remove
from multiprocessing import Pool
import re
from codecs import open
from os.path import dirname, exists, relpath, abspath, basename
from os.path import join as join_path
from sys import platform
from functools import partial
from json_tools import prepare, field_by_path, list_field_paths


def export_memory(path, memory_file):
    memory = dict()
    for path, d, filelist in walk(path):
        for filename in filelist:
            if basename(filename) in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt", "_metadata", "_previewimage", "memory.json"]:
                continue
            i = join_path(path, filename)
            print(basename(i))
            with open(i, "rb+", "utf-8") as f:
                jsondata = json.loads(prepare(f))
                for i, v in enumerate(jsondata):
                    if 'Chs' in jsondata[i]['Texts']:
                        if jsondata[i]['Texts']['Eng'] in memory.keys():
                            pass
                        elif jsondata[i]['Texts']['Eng'] == jsondata[i]['Texts']['Chs']:
                            pass
                        else:
                            memory[jsondata[i]['Texts']['Eng']
                                   ] = jsondata[i]['Texts']['Chs']
                    else:
                        pass
    result = json.dumps(memory, ensure_ascii=False,
                        sort_keys=True, indent=2)
    f = open(memory_file, "wb+", "utf-8")
    f.write(result)
    f.close


def import_memory(path, memory_file):
    memory = json.loads(prepare(open(memory_file, "r", "utf-8")))
    for path, d, filelist in walk(path):
        for filename in filelist:
            if basename(filename) in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt", "_metadata", "_previewimage", "memory.json"]:
                continue
            i = join_path(path, filename)
            print(basename(i))
            with open(i, "rb+", "utf-8") as f:
                jsondata = json.loads(prepare(f))
                for t, v in enumerate(jsondata):
                    if 'Chs' in jsondata[t]['Texts']:
                        pass
                    else:
                        if jsondata[t]['Texts']['Eng'] in memory.keys():
                            jsondata[t]['Texts']['Chs'] = memory[jsondata[t]
                                                                 ['Texts']['Eng']]
            text = json.dumps(jsondata, ensure_ascii=False,
                                  sort_keys=True, indent=2)     
            f = open(i, "wb+", "utf-8")
            f.write(text)
            f.close

def import_memory_para(path, memory_file):
    memory = json.loads(prepare(open(memory_file, "r", "utf-8")))
    for path, d, filelist in walk(path):
        for filename in filelist:
            if basename(filename) in ["substitutions.json", "totallabels.json", "translatedlabels.json", "patch_substitutions.json", "parse_problem.txt", "_metadata", "_previewimage", "memory.json","translations_bak.zip"]:
                continue
            i = join_path(path, filename)
            print(basename(i))
            with open(i, "rb+", "utf-8") as f:
                jsondata = json.loads(prepare(f))
                for t, v in enumerate(jsondata):
                    if jsondata[t]['translation'] != "":
                        pass
                    else:
                        if jsondata[t]['original'] in memory.keys():
                            jsondata[t]['translation'] = memory[jsondata[t]['original']]
            text = json.dumps(jsondata, ensure_ascii=False,
                                  sort_keys=True, indent=2)     
            f = open(i, "wb+", "utf-8")
            f.write(text)
            f.close

#ge_walk("F:/workplace/StarBound_-Mod_Misc_Chinese_Project/text/Project Knightfall","F:/workplace/StarBound_-Mod_Misc_Chinese_Project/text/Project Knightfall/memory.json")
#export_memory("F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re-101a18e40e5ad232315ba1201e5dfc0ac7a4a67b/translations","F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/translations/memory.json")
import_memory_para("F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/translations","F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/translations/memory.json")

