#creating project structure
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')



list_of_files=[
    '.github/workflows/main.yaml',
    'Templates/home.html',
    'Templates/results.html',
    'Model/standardScalar.pkl',
    'Model/modelForPrediction.pkl',
    'app.py',
    'requirements.txt',
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating file directory:{filedir} for {filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'Creating empty file {filepath}')
    else:
        logging.info(f'{filename} already exist')