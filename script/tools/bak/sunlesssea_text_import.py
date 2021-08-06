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

dir_text = "F:/sunlesssee/new/cn_translation/texts"
target = "F:/sunlesssee/target"


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def add_value(dict_obj, path, value):
    obj = dict_obj
    for i, v in enumerate(path):
        if is_int(v) is True:
            v = int(v)
        if i == 0:
            w = obj[v]
        elif i+1 < len(path):
            w = w[v]
        else:
            w[v] = value
            break
    return dict_obj


def sunlesssea_text_loader(un_dir, text_dir, target_dir):
    print("Sunless Sea text is loading")
    Associations_text = json.loads(
        prepare(open(un_dir+'/'+"encyclopaedia/Associations.json", "rb+", "utf-8")))
    CombatAttacks_text = json.loads(
        prepare(open(un_dir+'/'+"encyclopaedia/CombatAttacks.json", "rb+", "utf-8")))
    CombatItems_text = json.loads(
        prepare(open(un_dir+'/'+"encyclopaedia/CombatItems.json", "rb+", "utf-8")))
    SpawnedEntities_text = json.loads(
        prepare(open(un_dir+'/'+"encyclopaedia/SpawnedEntities.json", "rb+", "utf-8")))
    Tutorials_text = json.loads(
        prepare(open(un_dir+'/'+"encyclopaedia/Tutorials.json", "rb+", "utf-8")))
    areas_text = json.loads(
        prepare(open(un_dir+'/'+"entities/areas.json", "rb+", "utf-8")))
    events_text = json.loads(
        prepare(open(un_dir+'/'+"entities/events.json", "rb+", "utf-8")))
    exchanges_text = json.loads(
        prepare(open(un_dir+'/'+"entities/exchanges.json", "rb+", "utf-8")))
    qualities_text = json.loads(
        prepare(open(un_dir+'/'+"entities/qualities.json", "rb+", "utf-8")))
    Tiles_text = json.loads(
        prepare(open(un_dir+'/'+"geography/Tiles.json", "rb+", "utf-8")))
    print("Loading complete")
    for path, d, filelist in os.walk(text_dir):
        for filename in filelist:
            w = os.path.join(path, filename).replace('//', '/')
            json_data = json.loads(prepare(open(w, "rb+", "utf-8")))
            for i in json_data:
                if "Chs" in i["Texts"]:
                    file_list = i["Files"].keys()
                    for p in file_list:
                        path_list = i["Files"][p]
                        if p == "encyclopaedia/Associations.json":
                            for v in path_list:
                                Associations_text = add_value(Associations_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "encyclopaedia/CombatAttacks.json":
                            for v in path_list:
                                CombatAttacks_text = add_value(CombatAttacks_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "encyclopaedia/CombatItems.json":
                            for v in path_list:
                                CombatItems_text = add_value(CombatItems_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "encyclopaedia/SpawnedEntities.json":
                            for v in path_list:
                                SpawnedEntities_text = add_value(SpawnedEntities_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "encyclopaedia/Tutorials.json":
                            for v in path_list:
                                Tutorials_text = add_value(Tutorials_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "entities/areas.json":
                            for v in path_list:
                                areas_text = add_value(areas_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "entities/events.json":
                            for v in path_list:
                                events_text = add_value(events_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "entities/exchanges.json":
                            for v in path_list:
                                exchanges_text = add_value(exchanges_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "entities/qualities.json":
                            for v in path_list:
                                qualities_text = add_value(qualities_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
                        elif p == "geography/Tiles.json":
                            for v in path_list:
                                Tiles_text = add_value(Tiles_text, v.replace(
                                    '/', '', 1).split('/'), i["Texts"]["Chs"])
    print("Now,start to import text")
    Associations_mod = open(
        target_dir+'/'+"encyclopaedia/Associations.json", "wb+", "utf-8")
    CombatAttacks_mod = open(
        target_dir+'/'+"encyclopaedia/CombatAttacks.json", "wb+", "utf-8")
    CombatItems_mod = open(
        target_dir+'/'+"encyclopaedia/CombatItems.json", "wb+", "utf-8")
    SpawnedEntities_mod = open(
        target_dir+'/'+"encyclopaedia/SpawnedEntities.json", "wb+", "utf-8")
    Tutorials_mod = open(
        target_dir+'/'+"encyclopaedia/Tutorials.json", "wb+", "utf-8")
    areas_mod = open(target_dir+'/'+"entities/areas.json", "wb+", "utf-8")
    events_mod = open(target_dir+'/'+"entities/events.json", "wb+", "utf-8")
    exchanges_mod = open(
        target_dir+'/'+"entities/exchanges.json", "wb+", "utf-8")
    qualities_mod = open(
        target_dir+'/'+"entities/qualities.json", "wb+", "utf-8")
    Tiles_mod = open(target_dir+'/'+"geography/Tiles.json", "wb+", "utf-8")
    Associations_mod.write(json.dumps(
        Associations_text, ensure_ascii=False, sort_keys=True, indent=2))
    CombatAttacks_mod.write(json.dumps(
        CombatAttacks_text, ensure_ascii=False, sort_keys=True, indent=2))
    CombatItems_mod.write(json.dumps(
        CombatItems_text, ensure_ascii=False, sort_keys=True, indent=2))
    SpawnedEntities_mod.write(json.dumps(
        SpawnedEntities_text, ensure_ascii=False, sort_keys=True, indent=2))
    Tutorials_mod.write(json.dumps(
        Tutorials_text, ensure_ascii=False, sort_keys=True, indent=2))
    areas_mod.write(json.dumps(
        areas_text, ensure_ascii=False, sort_keys=True, indent=2))
    events_mod.write(json.dumps(
        events_text, ensure_ascii=False, sort_keys=True, indent=2))
    exchanges_mod.write(json.dumps(
        exchanges_text, ensure_ascii=False, sort_keys=True, indent=2))
    qualities_mod.write(json.dumps(
        qualities_text, ensure_ascii=False, sort_keys=True, indent=2))
    Tiles_mod.write(json.dumps(
        Tiles_text, ensure_ascii=False, sort_keys=True, indent=2))
    Associations_mod.close
    CombatAttacks_mod.close
    CombatItems_mod.close
    SpawnedEntities_mod.close
    Tutorials_mod.close
    areas_mod.close
    events_mod.close
    exchanges_mod.close
    qualities_mod.close
    Tiles_mod.close
    print("Import complete")


if __name__ == "__main__":
    sunlesssea_text_loader("F:/Sunless_Sea_Data/Sunless Sea_source_file",
                           "F:/Sunless_Sea_Chinese_Translation_Mod_Re/translations/texts", "F:/Sunless_Sea_Chinese_Translation_Mod_Re/release/Sunless_Sea_Chinese_Translation_Mod_Re")
