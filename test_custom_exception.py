from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger=get_logger(__name__)
def divide(a,b):
    try:
        result=a/b
        logger.info("dividing two numbers")
    except Exception as ce:
        logger.error("Error Occured")
        raise CustomException("Custom Error Ocurred",sys)
if __name__=="__main__":
    try:
        logger.info("starting a program")
        divide(10,0)
    except CustomException as ce:
        logger.error(str(ce))
    
    
    
