from fileinput import filename
import json
from operator import contains
import os
from os.path import isfile, join
jsonData = {}

file_name = "default"

with open(f"font/{file_name}.json", "r") as fontFile:
    jsonData = json.load(fontFile)


font_textures_path = "textures/font/"


fileNames = [i for i in os.listdir(font_textures_path) if os.path.isfile(os.path.join(font_textures_path, i)) ]


def write_providers(providers):
    with open(f"output_{file_name}.json", "w") as file:
        thing = {}
        thing["providers"] = providers
        json.dump(thing, file, indent=4)



def filter_fonts(font_data:dict, file_names):
    providers:list =  font_data["providers"]
    newProviders:list = []
    for provider in providers:
        if "file" in provider:
            needed_file_name_raw: str = provider["file"]
            needed_file_name = needed_file_name_raw.split("/")[1]
            if needed_file_name in file_names:
                newProviders.append(provider)
        else: 
            if "type" in provider:
                if provider["type"] == "space":
                    newProviders.append(provider)
    write_providers(newProviders)




filter_fonts(jsonData, fileNames)