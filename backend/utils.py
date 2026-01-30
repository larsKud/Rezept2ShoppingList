import pathlib
import json

def load_json(path: str):
    home = str(pathlib.Path(__file__).parent)
    with open(home + "/"+ path) as f:
        temp_dict = json.load(f)
        return temp_dict