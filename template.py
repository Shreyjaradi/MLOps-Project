import os 
from pathlib import Path
import logging

list_of_file = [".github/workflows/.gitkeep", 
                "src/__init__.py", 
                "src/components/__init__.py", 
                "src/components/data_integestion.py", 
                "src/components/data_transformation.py", 
                "src/components/model_trainer.py", 
                "src/components/model_evaluation.py",
                "src/pipeline/__init__.py",
                "src/pipeline/training_pipeline.py",
                "src/pipeline/prediction_pipeline.py",
                "src/utils/__inti__.py",
                "src/utils/utils.py",
                "src/logger/loggin.py",
                "src/exception/exception.py"
                "test/unit/__init__.py",
                "test/integeration/__init__.py",
                "init_setup.sh",
                "requirements.txt",
                "requirements_dev.txt",
                "setup.py"
                "setup.cfg",
                "pyproject.toml",
                "tox.ini",
                "experiment/experimentx.ipynb"]

for filepath in list_of_file:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating Directory: {filedir} for file : {filename} " )
        
        if (not os.path.exists(filepath))  or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass

    



