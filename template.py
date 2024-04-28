import os


list_of_files = [
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/data_evaluation.py",
    "src/components/model_trainer.py",
    "src/exception/exception.py",
    "src/logger/logging.py",
    "src/pipeline/prediction_pipeline.py"
    "src/pipeline/training_pipeline.py"
    "src/utils/utils.py",
    "app.py",
    "test.py",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "requirements.txt",
    "requirements-dev.txt",
]

for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
