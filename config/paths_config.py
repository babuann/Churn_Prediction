import os 
######### Data Ingestion###########
RAW_DIR="artifacts/raw"
RAW_FILE_PATH=os.path.join(RAW_DIR,"raw.csv")
TRAIN_FILE=os.path.join(RAW_DIR,"train.csv")
TEST_FILE=os.path.join(RAW_DIR,"test.csv")

CONFIG_PATH="config/config.yaml"

#### Data Processing
PROCESSED_DIR="arifacts/processed"
PROCESSED_TRAIN_DATA_PATH=os.path.join(PROCESSED_DIR,'processed_train_csv')
PROCESSED_TEST_DATA_PATH=os.path.join(PROCESSED_DIR,'processed_test_csv')

#########Model Training
MODEL_OUTPUT_PATH="artifacts/models/lgbm_model.pkl"
