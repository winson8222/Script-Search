import os
import json


def receive(fpath):
    path = fpath
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            if entry.find(".txt") != -1:
                f = open(os.path.join(path, entry), 'r')
                if f.read().find("Nehao") != -1:
                    print(entry)
        if os.path.isdir(os.path.join(path, entry)):
            receive(os.path.join(path, entry))


def search():
    folder_path = 'C:/TestFile/en-US'
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        print(file)
        with open(file_path, 'r') as f:
            try:
                f = f.read()
                f = f.replace('export default ', '')
                parsed_data = json.loads(f)
                print(parsed_data)
                # record(parsed_data)
            except:
                print(f"Error parsing file {file}: {json.JSONDecodeError}")


search()
