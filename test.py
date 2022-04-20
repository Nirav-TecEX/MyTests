import yaml
import os

cwd = os.getcwd()
yml_filename = "TestData.yml"
fullpath = os.path.join(cwd, "TestDocs" , yml_filename)

with open(fullpath, "r") as data_stream:
    try:
        data = yaml.safe_load(data_stream) 
        # print(data)
        print()
        print(f"TexExUsername: {data['TecExUsername']}")
    except yaml.YAMLError as exc:
        print(exc)
