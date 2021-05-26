import os
import yaml

def load_config():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open (root_dir + "/config.yaml", "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)

def get_files(dir):
    with os.scandir(dir) as files:
        for file in files:
            if file.is_file() and not file.name.startswith('.'):
                yield file