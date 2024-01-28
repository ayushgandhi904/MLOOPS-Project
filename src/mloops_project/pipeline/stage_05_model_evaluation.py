from mloops_project import logger
from pathlib import Path
from mloops_project.config.configuration import ConfigurationManager
from mloops_project.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        

if __name__ == "__main__":
    try:
        logger.info(f"---stage {STAGE_NAME}---")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()
        logger.info(f"---stage {STAGE_NAME} completed---")
    except Exception as e:
        logger.exception(e)
        raise e