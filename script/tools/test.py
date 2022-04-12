import jsonpatch
from json import dump, loads, dumps
from os.path import join, basename, dirname
def load(path):
    return loads(prepare(open(path, 'r', encoding="utf-8")))
from json_tools import prepare
"""
patch = jsonpatch.make_patch(load("/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/release/Sunless_Sea_Chinese_Translation_Mod_Re/entities/events.json"), load("F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/events copy.json"))
with open("F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/events copy.json.patch", "w+", encoding="utf-8") as f:
    dump(loads(patch.to_string()), f, ensure_ascii=False,
                                 indent=2, sort_keys=True)
"""
ru = load("/Sunless_Sea_Data/Russian/entities/qualities.json")
raw = load("/Sunless_Sea_Data/Sunless Sea_source_file/entities/qualities.json")
result = list()
for i in range(len(ru)) :
    if ru[i] == raw[i]:
        if ru[i]["Tag"] not in result:
            result.append(ru[i]["Tag"])
print(result)
