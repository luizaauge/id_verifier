import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    ENDPOINT = os.getenv('ENDPOINT')
    KEY = os.getenv('KEY')
    STORAGE_CONNECTION = os.getenv('STORAGE_CONNECTION')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')
    OBJECT_OD = os.getenv('OBJECT_ID')
