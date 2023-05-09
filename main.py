from credit.logger import logging
from credit.exception import creditException
from credit.utils import get_collection_as_dataframe
import sys,os
from credit.entity import config_entity
from credit.components.data_ingestion import DataIngestion
#from credit.components.data_validation import DataValidation

# Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

try:
     training_pipeline_config = config_entity.TrainingPipelineConfig()

     #data ingestion
     data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
     print(data_ingestion_config.to_dict())
     data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
     data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
     
        #data validation
      #  data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
      #  data_validation = DataValidation(data_validation_config=data_validation_config,
      #                  data_ingestion_artifact=data_ingestion_artifact)
      #  data_validation_artifact = data_validation.initiate_data_validation()
except Exception as e:
     raise creditException(e, sys)