import os
from pathlib import Path

project_name = "src"

list_of_files =[
    ## init file of src
    f"{project_name}/__init__.py",

    ## Components
    #  with all the components of data -> model pusher full pipeline
    # init file of components package
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",


    ## Configuration
    # for making connections with mongodb and aws
    # self __init__
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    ## Cloud storage 
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",

    ## Data access
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",

    ## Constants
    f"{project_name}/constant/__init__.py",

    ## Entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",

    ## Exception
    f"{project_name}/exception/__init__.py",

    ## Logger
    f"{project_name}/logger/__init__.py",

    ## PipeLine
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    ## Utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    ## Outside src 

    "app.py",
    "requiremnents.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]

## create whole template
for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    ## mean ki main directory main nahi hai
    ## filepath.parent , fiding the directory from filepath if 
    print(f"filepath.parent {filepath.parent}")

    if filepath.parent:
        filepath.parent.mkdir(parents=True, exist_ok=True)

    filepath.touch(exist_ok=True)


