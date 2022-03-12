#!/usr/bin/python3

from codecs import open as open_n_decode
from json import dump, load, loads, dumps
from multiprocessing import Pool
from os import makedirs, remove, walk
from os.path import abspath, basename, dirname, exists, join, relpath
from sys import platform
from json_tools import prepare
if platform == "win32":
    from os.path import normpath as normpath_old

    def normpath(path):
        return normpath_old(path).replace('\\', '/')
else:
    from os.path import normpath
root_dir = "/Sunless_Sea_Data/Sunless Sea_source_file"
prefix = "/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/translations"
black_list = [""]

def para_tranz(key, original, translation="", context=""):
    result = {"key": key, "original": original,
              "translation": translation, "context": context}
    return result


def export_json(file_path):
    list = []
    with open_n_decode(file_path, "r", "utf_8_sig") as f:
            string = prepare(f)
            jsondata = loads(string)
            if basename(file_path) == "Associations.json":
                for i in jsondata[0]["Ambiences"]:
                    if i["Name"] != "":
                        list.append(para_tranz(
                            i["Name"]+"##"+str(i["AreaId"])+"$Name&Ambiences", i["Name"]))
                for i in jsondata[0]["JettisonEvents"]:
                    if i["Name"] != None:
                        list.append(para_tranz(
                            i["Name"]+"##"+str(i["QualityId"])+"$Name&JettisonEvents", i["Name"]))
                    if i["Tooltip"] != None:
                        list.append(para_tranz(
                            i["Tooltip"]+"##"+str(i["QualityId"])+"$Tooltip&JettisonEvents", i["Tooltip"]))
                for i in jsondata[0]["LegacyUnlockQualities"]:
                    if i["Name"] != None:
                        list.append(para_tranz(
                            i["Name"]+"##"+str(i["Order"])+"$Name&LegacyUnlockQualities", i["Name"]))
                    if i["Description"] != None:
                        list.append(para_tranz(
                            i["Description"]+"##"+str(i["Order"])+"$Description&LegacyUnlockQualities", i["Description"]))
                    if i["Tooltip"] != None:
                        list.append(para_tranz(
                            i["Tooltip"]+"##"+str(i["Order"])+"$Tooltip&LegacyUnlockQualities", i["Tooltip"]))
                for i in jsondata[0]["UnlegacyableOfficers"]:
                    if i["Name"] != None:
                        list.append(para_tranz(
                            i["Name"]+"##"+str(i["QualityId"])+"$Name&UnlegacyableOfficers", i["Name"]))
            elif basename(file_path) == "CombatAttacks.json":
                for i in jsondata:
                    if i["Description"] != None:
                        list.append(para_tranz(
                            i["Name"]+"$Description", i["Description"]))
            elif basename(file_path) == "SpawnedEntities.json":
                for i in jsondata:
                    if i["HumanName"] != None:
                        list.append(para_tranz(
                            i["Name"]+"$HumanName", i["HumanName"]))
            elif basename(file_path) == "Tutorials.json":
                for i in jsondata:
                    if i["Name"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Name", i["Name"]))
                    if i["Description"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Description", i["Description"]))
            elif basename(file_path) == "areas.json":
                for i in jsondata:
                    if i["Name"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Name", i["Name"]))
                    if i["Description"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Description", i["Description"]))
                    if i["MoveMessage"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$MoveMessage", i["MoveMessage"]))
            elif basename(file_path) == "events.json":
                for i in jsondata:
                    if i["Name"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Name", i["Name"]))
                    if i["Description"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Description", i["Description"]))
                    if i["Teaser"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Teaser", i["Teaser"]))
                    
                    if i["ChildBranches"] != None:
                        for x in i["ChildBranches"]:
                            if x["Name"] != None:
                                list.append(para_tranz(
                                    str(i["Id"])+"/"+str(x["Id"])+"$Name", x["Name"]))
                            if x["Description"] != None:
                                list.append(para_tranz(
                                    str(i["Id"])+"/"+str(x["Id"])+"$Description", x["Description"]))
                            if x["ButtonText"] != None :
                                if x["ButtonText"] != "":
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"$ButtonText", x["ButtonText"]))
                            if x["SuccessEvent"] != None:
                                y = x["SuccessEvent"]
                                if y["Name"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%SuccessEvent$Name", y["Name"]))
                                if y["Description"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%SuccessEvent$Description", y["Description"]))
                                if y["Teaser"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%SuccessEvent$Teaser", y["Teaser"]))
                            if x["DefaultEvent"] != None:
                                y = x["DefaultEvent"]
                                if y["Name"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%DefaultEvent$Name", y["Name"]))
                                if y["Description"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%DefaultEvent$Description", y["Description"]))
                                if y["Teaser"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%DefaultEvent$Teaser", y["Teaser"]))
                                if y["MoveToArea"] != None:
                                    if y["MoveToArea"]["Description"] != None:
                                        list.append(para_tranz(
                                            str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"/"+str(y["MoveToAreaId"])+"%MoveToArea$Description", y["MoveToArea"]["Description"]))
                                    if y["MoveToArea"]["Name"] != None:
                                        list.append(para_tranz(
                                            str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"/"+str(y["MoveToAreaId"])+"%MoveToArea$Name", y["MoveToArea"]["Name"]))
                            if x["RareDefaultEvent"] != None:
                                y = x["RareDefaultEvent"]
                                if y["Name"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%RareDefaultEvent$Name", y["Name"]))
                                if y["Description"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%RareDefaultEvent$Description", y["Description"]))
                                if y["Teaser"] != None:
                                    list.append(para_tranz(
                                        str(i["Id"])+"/"+str(x["Id"])+"/"+str(y["Id"])+"%RareDefaultEvent$Teaser", y["Teaser"]))
            elif basename(file_path) == "exchanges.json":
                for i in jsondata:
                    if i["Name"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Name", i["Name"]))
                    if i["Description"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Description", i["Description"]))
                    if i["Shops"] != None:
                        for x in i["Shops"]:
                            if x["Name"] != None:
                                list.append(para_tranz(
                                    str(i["Id"])+"/"+str(x["Id"])+"%Shops$Name", x["Name"]))
                            if x["Description"] != None:
                                list.append(para_tranz(
                                    str(i["Id"])+"/"+str(x["Id"])+"%Shops$Description", x["Description"]))
            elif basename(file_path) == "qualities.json":
                for i in jsondata:
                    if i ["Tag"] in ["Ship Equipment Slot","Ship Conditions"]:
                        continue
                    if i["Name"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Name", i["Name"]))
                    if i["Description"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$Description", i["Description"]))
                    if i["LevelDescriptionText"] != None:
                        list.append(para_tranz(
                            str(i["Id"])+"$LevelDescriptionText", i["LevelDescriptionText"]))
            elif basename(file_path) == "Tiles.json":
                for i in jsondata:
                    if i["Tiles"] != None:
                        for x in i["Tiles"]:
                            if x["HumanName"] != None:
                                list.append(para_tranz(
                                    str(i["Name"])+"$HumanName", x["HumanName"]))
                            if x["Description"] != None:
                                list.append(para_tranz(
                                    str(i["Name"])+"$Description", x["Description"]))
                            if x["LabelData"] != None:
                                for y in x["LabelData"]:
                                    if y["Label"] != None:
                                        list.append(para_tranz
                                                    (str(i["Name"])+"/" +str(y["Label"])+"%"+"LabelData$Label", y["Label"]))
            else:
                return None
    return list


if __name__ == '__main__':
    print("Scanning assets at " + root_dir)
    for subdir, dirs, files in walk(root_dir):
        for thefile in files:
            if basename(thefile) in ["Associations.json","CombatAttacks.json","SpawnedEntities.json","Tutorials.json","areas.json","events.json","exchanges.json","qualities.json","Tiles.json"]:
                print(basename(thefile))
                result = export_json(normpath(join(subdir, thefile)))
                if result is not None:
                    export_file = normpath(
                        join(subdir, thefile)).replace(root_dir, prefix)
                    filedir = dirname(export_file)
                    if len(filedir) > 0:
                        makedirs(filedir, exist_ok=True)
                    if exists(export_file):
                        with open_n_decode(export_file, 'r', 'utf-8') as g:
                            olddata = load(g)
                        if olddata == result:
                            pass
                        else:
                            for newdata in range(len(result)):
                                for i in olddata:
                                    if i["key"] == result[newdata]["key"] and  i["original"] ==  result[newdata]["original"]  and  i["translation"]!=None:
                                        result[newdata]["translation"] = i["translation"]
                                        continue
                    with open_n_decode(export_file, "w", 'utf-8') as f:
                        dump(result, f, ensure_ascii=False,
                            indent=2, sort_keys=True)
