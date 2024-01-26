from mloops_project import logger
from mloops_project.config.configuration import ConfigurationManager
from mloops_project.components.data_validation import DataValiadtion

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f"---stage {STAGE_NAME}---")
        data_validation = DataValidationPipeline()
        data_validation.main()
        logger.info(f"---stage {STAGE_NAME} completed---")
    except Exception as e:
        logger.exception(e)
        raise e