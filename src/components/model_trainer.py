import sys
from typing import Tuple

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import load_numpy_array_data, load_object, save_object

from src.entity.config_entity import ModelTrainerConfig
from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact, ClassificationMetricArtifact
from src.entity.estimator import MyModel

class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact,
                 model_trainer_config : ModelTrainerConfig):
       
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config

    def get_model_object_and_report(self, train:np.array, test:np.array ) -> Tuple[object,object]:
        """
        Docstring for get_model_object_and_report
        
        
        :param train: train data retrieved from transformed step
        :type train: np.array

        :param test: test data retrieved from transformed step
        :type test: np.array
        :return: Metrics artifact  and Trained Model object
        :rtype: Tuple[object, object]
        """
        try:
            logging.info("Training RandomForestClassifier with specified Parameters")

            # spliting thre train and test data into features and targets
            X_train, y_train, X_test, y_test = train[:,:-1], train[:,-1], test[:,:-1], test[:,-1]
            logging.info("X, y split done")

            # Model Initialization 
            model  = RandomForestClassifier(
                n_estimators=self.model_trainer_config._n_estimators,
                min_samples_split= self.model_trainer_config._min_samples_split,
                min_samples_leaf=self.model_trainer_config._min_samples_leaf,
                max_depth= self.model_trainer_config._max_depth,
                criterion= self.model_trainer_config._criterion,
                random_state=self.model_trainer_config._random_state

            )
            # fit the Model
            logging.info("Model Training begins !!")
            model.fit(X_train, y_train)
            logging.info("Model Training completed")

            # Predictions and evaluation metrics
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test,y_pred)
            f1 = f1_score(y_test, y_pred)
            precision =precision_score(y_test,y_pred)
            recall = recall_score(y_test, y_pred)

            # Creating Meric Artifact
            metric_artifact = ClassificationMetricArtifact(accuracy_score=accuracy,f1_score=f1, precision_score=precision,recall_score=recall)

            return model, metric_artifact

        except Exception as e:
            raise MyException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        """
        Create My Model Object with  (Trained Model Object and preprocessed pipeline object) in it 
        save that object to path  in model_trainer_config. 
        :return:  ModelTrainerArtifact with path and metric                                                                          
        :rtype: ModelTrainerArtifact
        """

        try:
            print("--------------------------------------------------------------------------")
            print("Startin Model Trainer Component")

            # loading transformed train and test data
            train_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_arr= load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_file_path)
            logging.info("train test data loaded")\
            
            # Trained Model and metric artifact 
            trained_model, metric_artifact = self.get_model_object_and_report(train=train_arr, test=test_arr)
            logging.info("Model object and artifact loaded")

            # load preprocessing object
            preprocessing_obj   = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)
            logging.info("Processinh Object loaded")

            # check if the model Accuracy meet the expected threshold
            X_train  = train_arr[:,:-1]
            y_train  = train_arr[:,-1]
            y_train_pred = trained_model.predict(X_train)
            accuracy_score_train = accuracy_score(y_train,y_train_pred)

            if accuracy_score_train < self.model_trainer_config.expected_accuracy:
                logging.info("No Model found with score above the base score")
                raise Exception("No Model found with the base score above the base score")

            # Save the final Model Object that includes both preprocessing and the trained Model
            logging.info("Saving new Model as performance in better than base score")
            my_model =MyModel(preprocessing_object=preprocessing_obj,trained_model_object=trained_model)
            save_object(self.model_trainer_config.trained_model_file_path, my_model)
            logging.info("Saved Final Model object that includes both preprocessing and the trained Model")

            # Create and return the ModelTrainerArtifact
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                metric_artifact=metric_artifact,
            )
            logging.info(f"Model Trainer Artifact :{model_trainer_artifact}")

            return model_trainer_artifact
        
        except Exception as e:
            raise MyException(e, sys)

       