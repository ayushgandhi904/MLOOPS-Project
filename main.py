from mloops_project import logger
from mloops_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"---stage {STAGE_NAME}---")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"---stage {STAGE_NAME} completed---")
except Exception as e:
    logger.exception(e)
    raise e