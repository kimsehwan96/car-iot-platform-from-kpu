# TODO:
# Make csv files
# Save csv file in local
# Upload csv file to S3
import csv
import pandas
import os
from .base_dispatcher import BaseDispatcher

LOCAL_DATA_PATH = '/kpu/rawdata'


class StorageDispatcher(BaseDispatcher):
    def __init__(self):
        if not os.path.exists(LOCAL_DATA_PATH):
            os.makedirs(LOCAL_DATA_PATH)

    def write_csv(self, filepath, data):
        pass

    def copy_to_s3(self, files, objects):
        pass

    def save_and_upload(self, values):
        pass

    def relay(self, data: str):
        pass
