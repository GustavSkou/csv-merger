import json

width = 500     # x
height = 285    # y

config_keys = ["folder_location", "file_name", "concat_file_location", "Index", "header"]
config_entries_keys = ["folder_location", "file_name", "concat_file_location"]
config_checkbuttons_keys = ["Index", "header"]

def json_write():
    json_object = json.dumps(config_dict, indent=4)

    with open("config.json", "w") as outfile:
        outfile.write(json_object)


def json_read(str):
    with open("config.json") as openfile:
        json_object = json.load(openfile)
        return json_object[str]


def get_config():
    with open("config.json") as openfile:
        json_object = json.load(openfile)
        return json_object


config_dict = get_config()
