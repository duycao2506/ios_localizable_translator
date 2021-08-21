# -*- coding: utf-8 -*-

import argparse
import os
import mmap
import re
import pip
import io
from pip._internal.utils.misc import get_installed_distributions
from pathlib import Path

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def append_to_file(text):
    f = open(args.output+".strings", "a+")
    f.write(text+"\n")
    f.close()

def append_to_file_dest(text, dest):
    f = open(args.output+"_"+dest+".strings", "a+")
    # text = text.encode('utf-8')
    f.write(text+"\n")
    f.close()

# def findAndTranslateIn(dir, outf):


# check installed packages
installed_packages = get_installed_distributions()
flat_installed_packages = [package.project_name for package in installed_packages]

# parse args
parser = argparse.ArgumentParser()
parser.add_argument("directory", help="the directory to search localizable strings in")
parser.add_argument("--output", default="Localizable", help="the file (without extension) to output the localizable strings")
parser.add_argument("--no-comments", action='store_true', help="use this to skip comments on the localizable strings")
parser.add_argument("--locale-origin", help="set the origin locale for auto translation")
parser.add_argument("--locale-target", help="set the target locale for auto translation")
args = parser.parse_args()

print("ok10")

# check if you need to translate
if args.locale_origin and args.locale_target:
    if 'googletrans' not in flat_installed_packages:
        print("Installing googletrans... ")
        install('googletrans==4.0.0rc1')
    from googletrans import Translator
    translator = Translator()
    print("ok1")
else:
    print("locale-origin and locale-target are both needed for translation")

# get swift files in directory
for path in Path(args.directory).rglob('*.swift'):
    print(path.absolute().as_posix())
    print("ok11")
    print("ok11 nè")
    f = path.absolute().as_posix()
    print("Searching... " + f)
    # with open(f, 'r+') as f:
    with io.open(f, 'rb') as f:
        data = f.read().decode('utf-8')#mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)#mmap.mmap(f.fileno(), 0)#.decode("utf-8")
        # print(data)
        # /NSLocalizedString\((.*)\)/gm
        results = re.finditer('NSLocalizedString\(\"(.*)\"\)', data)
        # print("ok12", len(results))
        if results:
            print("res chu7a")
            for result in results:
                print("res nè")
                result = result.group(1).replace("value:","").replace("comment:","")
                result = re.sub(r'\",(\s*)\"', '","', result)
                groups = result.split('","')
                value = groups[0].replace("\"","").strip()
                print(value, "key ne")
                comment = groups[1].strip()
                print(comment, "va ne")
                # comment = groups[2].strip()
                if args.no_comments:
                    trans = ""
                    trans_dest = ""
                else:
                    trans = "/* " + comment + " */\n"
                    trans_dest = "/* " + comment + " */\n"
                trans += "\"" + value + "\" = \"" + value + "\";\n"
                append_to_file(trans)
                print(trans, " trans nè ")
                if args.locale_origin and args.locale_target:
                    value_dest = ""
                    try:
                        obj = translator.translate(value, src=args.locale_origin, dest=args.locale_target)
                        value_dest = obj.text
                    except error:
                        value_dest = value
                        print(error)
                    trans_dest += "\"" + value + "\" = \"" + value_dest + "\";\n"
                    append_to_file_dest(trans_dest, args.locale_target)
                print("found translation: " + value)
        
