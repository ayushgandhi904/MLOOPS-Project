# MLOOPS-Project
End-to-end MLOOPS on red wine quality prediction

### Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update configuration 
6. Update components
7. Update pipeline
8. Update main.py
8. Update dvc.yaml

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/ayushgandhi904/MLOOPS-Project.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p venv python=3.9 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI= https://dagshub.com/ayushgandhi904/MLOOPS-Project.mlflow \
MLFLOW_TRACKING_USERNAME=ayushgandhi904 \
MLFLOW_TRACKING_PASSWORD=3aaf0a139bb1f0dae8decd9e11e0bbe95af194b4 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI= https://dagshub.com/ayushgandhi904/MLOOPS-Project.mlflow 

export MLFLOW_TRACKING_USERNAME=ayushgandhi904

export MLFLOW_TRACKING_PASSWORD= 3aaf0a139bb1f0dae8decd9e11e0bbe95af194b4

```