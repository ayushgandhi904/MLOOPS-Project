from mloops_project import logger
from mloops_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mloops_project.pipeline.stage_02_data_validation import DataValidationPipeline
from mloops_project.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mloops_project.pipeline.stage_04_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"---stage {STAGE_NAME}---")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"---stage {STAGE_NAME} completed---")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"---stage {STAGE_NAME}---")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f"---stage {STAGE_NAME} completed---")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"---stage {STAGE_NAME}---")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f"---stage {STAGE_NAME} completed---")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"---stage {STAGE_NAME}---")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"---stage {STAGE_NAME} completed---")
except Exception as e:
    logger.exception(e)
    raise e