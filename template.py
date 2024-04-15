import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(activate)s]:%(message)s:')

# Creating folder architecture

list_of_files = [
    
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trails.ipynb"
    
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for the files: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        print(f"file is already present at: {filepath}")
        logging.info (f"{filename} already exists")