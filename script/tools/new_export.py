from bisect import insort_left
from codecs import open as open_n_decode
from json import dump, load, loads, dumps
from multiprocessing import Pool
from os import makedirs, remove, walk
from os.path import abspath, basename, dirname, exists, join, relpath
from re import compile as regex
from sys import platform

from patch_tool import trans_patch, to_a_list
from ignore_file import ignore_filelist
from blacklist import dir_blacklist, path_blacklist
from json_tools import field_by_path, list_field_paths, prepare
from parser_settings import files_of_interest
from shared_path import getSharedPath
from special_cases import specialSections
from utils import get_answer

import traceback
if platform == "win32":
    from os.path import normpath as normpath_old

    def normpath(path):
        return normpath_old(path).replace('\\', '/')
else:
    from os.path import normpath
root_dir = "F:/Sunless_Sea_Data/Sunless Sea_source_file"
prefix = "F:/workplace/Sunless_Sea_Chinese_Translation_Mod_Re/translations1"
export_dir = ""
print("Scanning assets at " + prefix)
for subdir, dirs, files in walk(prefix):
    for thefile in files:
        """
        if subdir.replace('\\', '/').replace(root_dir, "") in dir_blacklist:
            break
        """
        if thefile.endswith(".json"):
            print(basename(normpath(join(subdir, thefile))))

            result = import_json(normpath(join(subdir, thefile))) #to-do
            if result is not None:
                export_file = normpath(join(subdir, thefile)).replace(root_dir,prefix)
                filedir = dirname(export_file)
                if len(filedir) > 0:
                    makedirs(filedir, exist_ok=True)
                if exists(export_file):
                    with open_n_decode(export_file, 'r', 'utf-8') as g:
                        olddata = load(g)
                    if olddata == result:
                        pass
                    else:
                        for i in olddata:
                            temp = i
                            temp["translation"]=""
                            temp["context"]=""
                            if temp in result:
                                result.remove(temp)
                        if len(result)>0:
                            olddata = olddata + result
                        result = olddata
                with open_n_decode(export_file, "w", 'utf-8') as f: 
                        dump(result, f, ensure_ascii=False, indent=2, sort_keys=True)