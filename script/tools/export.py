from codecs import open as open_n_decode
import re
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
root_dir = "/Sunless_Sea_Data/Sunless Sea_source_file"#无光之海的源文本目录
prefix = "/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/translations"#翻译文件所在目录
dump_dir = "/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/release/Sunless_Sea_Chinese_Translation_Mod_Re"#成品输出目录
def export_json(prefix,root_dir,dump_dir,file_path):
    with open_n_decode(file_path, "r", "utf_8_sig") as f:
            string = prepare(f)
            jsondata = loads(string)
            if basename(file_path) in ["Associations.json","CombatAttacks.json","SpawnedEntities.json","Tutorials.json","areas.json","events.json","exchanges.json","qualities.json","Tiles.json"]:
                raw_data = loads(prepare(open_n_decode(file_path.replace(prefix,root_dir), "r", "utf_8_sig")))
                result = raw_data
                if basename(file_path) == "Associations.json":
                    for data in jsondata:
                        if data ["translation"] != "" and data ["translation"] != data["original"]:
                            temp = re.search("(.*)##(.*)\$(.*)&(.*)",data["key"])
                            for i in range(len(raw_data[0][temp.group(4)])):
                                if raw_data[0][temp.group(4)][i][temp.group(3)] == temp.group(1) :
                                        if temp.group(4) == "Ambiences":
                                            if str(raw_data[0][temp.group(4)][i]["AreaId"]) == temp.group(2):
                                                result[0][temp.group(4)][i][temp.group(3)] = data ["translation"]
                                                continue
                                        elif temp.group(4) == "JettisonEvents" or temp.group(4) == "UnlegacyableOfficers":
                                            if str(raw_data[0][temp.group(4)][i]["QualityId"]) == temp.group(2):
                                                result[0][temp.group(4)][i][temp.group(3)] = data ["translation"]
                                                continue
                                        elif temp.group(4) == "LegacyUnlockQualities":
                                            if str(raw_data[0][temp.group(4)][i]["Order"]) == temp.group(2):
                                                result[0][temp.group(4)][i][temp.group(3)] = data ["translation"]
                                                continue                                                                           
                elif basename(file_path) in ["CombatAttacks.json","SpawnedEntities.json"]:
                    for data in jsondata:
                        if data ["translation"] != "" and data ["translation"] != data["original"]:
                            temp = re.search("(.*)\$(.*)",data["key"])
                            for i in range(len(raw_data)):
                                if raw_data[i]["Name"] == temp.group(1):
                                        result[i][temp.group(2)] = data ["translation"] 
                                        continue                                
                elif basename(file_path) in ["Tutorials.json","areas.json","qualities.json"]:
                    for data in jsondata:
                        if data ["translation"] != "" and data ["translation"] != data["original"]:
                            temp = re.search("(.*)\$(.*)",data["key"])
                            for i in range(len(raw_data)):
                                if str(raw_data[i]["Id"]) == temp.group(1):
                                        result[i][temp.group(2)] = data ["translation"]  
                                        continue
                elif basename(file_path) == "events.json":
                    for data in jsondata:
                        if data ["translation"] != "" and data ["translation"] != data["original"]:
                            temp = re.search("(.*)\$(.*)",data["key"])
                            if temp.group(1).endswith("%SuccessEvent") is False and temp.group(1).endswith("%DefaultEvent") is False and temp.group(1).endswith("%RareDefaultEvent") is False and temp.group(1).endswith("%MoveToArea") is False:
                                path = temp.group(1).split("/")
                                if len(path)==1:
                                        for i in range(len(raw_data)):
                                            if str(raw_data[i]["Id"]) == path[0]:
                                                result[i][temp.group(2)] = data ["translation"]  
                                                continue
                                elif len(path)==2:
                                        for i in range(len(raw_data)):
                                            if str(raw_data[i]["Id"]) == path[0]:
                                                for x in range(len(raw_data[i]["ChildBranches"])):
                                                    if str(raw_data[i]["ChildBranches"][x]["Id"]) == path[1]:
                                                        result[i]["ChildBranches"][x][temp.group(2)] = data ["translation"]  
                                                continue
                            else:
                                temp2 = re.search("(.*)\%(.*)",temp.group(1))
                                path = temp2.group(1).split("/")
                                if len(path)==3:
                                        for i in range(len(raw_data)):
                                            if str(raw_data[i]["Id"]) == path[0]:
                                                for x in range(len(raw_data[i]["ChildBranches"])):
                                                    if str(raw_data[i]["ChildBranches"][x]["Id"]) == path[1]:
                                                        if str(raw_data[i]["ChildBranches"][x][temp2.group(2)]["Id"]) == path[2]:
                                                                result[i]["ChildBranches"][x][temp2.group(2)][temp.group(2)] = data ["translation"]
                                elif len(path)==4 and temp2.group(2) == "MoveToArea":
                                        for i in range(len(raw_data)):
                                            if str(raw_data[i]["Id"]) == path[0]:
                                                for x in range(len(raw_data[i]["ChildBranches"])):
                                                    if str(raw_data[i]["ChildBranches"][x]["Id"]) == path[1] :
                                                        if str(raw_data[i]["ChildBranches"][x]["DefaultEvent"]["Id"]) == path[2] and str(raw_data[i]["ChildBranches"][x]["DefaultEvent"]["MoveToAreaId"]) == path[3]:
                                                                result[i]["ChildBranches"][x]["DefaultEvent"]["MoveToArea"][temp.group(2)] = data ["translation"]
                elif basename(file_path) == "exchanges.json":
                    for data in jsondata:
                        if data ["translation"] != "" and data ["translation"] != data["original"]:
                            temp = re.search("(.*)\$(.*)",data["key"])
                            if temp.group(1).endswith("%Shops") is False:
                                for i in range(len(raw_data)):
                                        if str(raw_data[i]["Id"]) == temp.group(1):
                                            result[i][temp.group(2)] = data ["translation"]  
                                            continue   
                            else:
                                temp2 = re.search("(.*)\%(.*)",temp.group(1))
                                path = temp2.group(1).split("/")
                                if len(path)==2:
                                        for i in range(len(raw_data)):
                                            if str(raw_data[i]["Id"]) == path[0]:
                                                for x in range(len(raw_data[i]["Shops"])):
                                                    if str(raw_data[i]["Shops"][x]["Id"]) == path[1]:
                                                        result[i]["Shops"][x][temp.group(2)] = data ["translation"]  
                                                continue
                elif basename(file_path) == "Tiles.json":
                    for data in jsondata:
                        if data ["translation"] != "" and data ["translation"] != data["original"]:
                            temp = re.search("(.*)\$(.*)",data["key"])
                            if temp.group(1).endswith("%"+"LabelData") is False:
                                for i in range(len(raw_data)):
                                        for x in range(len(raw_data[i]["Tiles"])):
                                            if str(raw_data[i]["Tiles"][x]["Name"]) == temp.group(1):
                                                result[i]["Tiles"][x][temp.group(2)] = data ["translation"]  
                                                continue
                            else:
                                temp2 = re.search("(.*)\%(.*)",temp.group(1))
                                for i in range(len(raw_data)):
                                        for x in range(len(raw_data[i]["Tiles"])):
                                            if raw_data[i]["Tiles"][x]["Name"] == temp2.group(1):
                                                for y in range(len(raw_data[i]["Tiles"][x]["LabelData"])):
                                                    if raw_data[i]["Tiles"][x]["LabelData"][y][temp.group(2)] == data["original"]:
                                                        result[i]["Tiles"][x]["LabelData"][y][temp.group(2)] = data ["translation"]
                                                    continue
                            
                                                 
                if result is not None:
                    export_file = file_path.replace(prefix,dump_dir)
                    filedir = dirname(export_file)
                    if len(filedir) > 0:
                        makedirs(filedir, exist_ok=True) 
                    with open_n_decode(export_file, "w", 'utf-8') as f: 
                            dump(result, f, ensure_ascii=False, indent=2, sort_keys=True)
            else:
                return None
    return result
    
export_json(prefix,root_dir,dump_dir,"F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/translations/geography/Tiles.json") 
if __name__ == '__main__':
    print("Exporting mod...")
    for subdir, dirs, files in walk(prefix):
        for thefile in files:
            if thefile.endswith(".json"):
                result = export_json(prefix,root_dir,dump_dir,normpath(join(subdir, thefile)))            