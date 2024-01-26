from mloops_project import logger
from mloops_project.config.configuration import ConfigurationManager
from mloops_project.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
if __name__ == "__main__":
    try:
        logger.info(f"---stage {STAGE_NAME}---")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f"---stage {STAGE_NAME} completed---")
    except Exception as e:
        logger.exception(e)
        raise e