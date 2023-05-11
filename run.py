import os
import pandas as pd
import traceback

# [0] is the key columns, [1] is the value columns, [2] a the list of paths
array = [[], [], []]

# find all the instance of the key used in the pages folder


def receive(fpath, key, value, row):
    path = fpath

    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            if entry.find(".js") != -1:
                f = open(os.path.join(path, entry), 'r', encoding='utf8')
                if f.read().find('\'' + key + '\'') != -1:
                    curpath = os.path.join(path, entry)[13:]
                    # number 13 is cuz my current path of pages is 'C:/PageFiles/pages' so the C:/... is spliced away to give pages/...
                    # modify it based on your own path
                    array[2][row].append(curpath.replace("\\", "/"))
                    print(entry, key, value, os.path.join(path, entry)[13:])
        if os.path.isdir(os.path.join(path, entry)):
            receive(os.path.join(path, entry), key, value, row)


def search():
    # the path to the key and value file in csv (Modify based own on path)
    folder_path = 'C:/TestFile/en-US'
    # the path to the pages folders (Modify based own on path)
    path = 'C:/PageFiles/pages'
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        print(file)
        with open(file_path, 'r', encoding='utf8') as f:
            try:
                data = pd.read_csv(
                    f, usecols=[0, 1], encoding_errors='ignore', encoding="utf8")
                data = data.dropna()  # drop NaN
                df = pd.DataFrame(data)
                # for value in df['Column3']:
                #     receive(path, value)
                for index, row in df.iterrows():  # Loop through Column 3 and 5
                    key = row[0]
                    value = row[1]
                    array[0].append(key)
                    array[1].append(value)
                    array[2].append([])
                    receive(path, key, value, index)
                print(array)  # Final Array
            except Exception as e:
                print(f"Error reading file '{file_path}':")
                print(traceback.format_exc())


search()
