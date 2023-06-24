import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project_name = "cnnClassifier"
project_name = "cnnCloud"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "param.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py",
    "templates/index.html"
]

for filepath in list_of_files:
    # Path / forward slash for Linux
    # So Path converts and tells that it is windows path
    # path = "config/config.yaml"
    filepath = Path(filepath)
    # WindowsPath('config/config.yaml')
    filedir, filename = os.path.split(filepath)
    # ('config', 'config.yaml')
    # (filedir, filename)
    if filedir != "":
        # exist_of = True if exists lefts out or else creates a new dir
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # os.path.getsize("README.MD") # 32
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
