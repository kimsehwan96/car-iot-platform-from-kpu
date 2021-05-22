import os
import boto3
import botocore
import logging
import json
from botocore.exceptions import ClientError
import time
import re

LOGGER = logging.getLogger()


class Client:
    IS_INIT_CREDENTIAL = False

    def __init__(self, name: str, **kwargs):
        if not name:
            raise Exception("Boto3 client name is emtpy")
        self.name = name

        self.client = boto3.client(name, **kwargs)

    @classmethod
    def set_boto3_config(cls, aws_profile=None, region_name=None) -> bool:
        if cls.IS_INIT_CREDENTIAL:
            return
        if os.environ.get('AWS_PROFILE'):
            LOGGER.info("Profile Environment Variable AWS_PROFILE : %s", os.environ.get('AWS_PROFILE'))
            return True
        if region_name:
            os.environ['AWS_DEFAULT_REGION'] = region_name
        if os.environ.get('AWS_ACCESS_KEY_ID') and os.environ.get('AWS_SECRET_ACCESS_KEY'):
            LOGGER.info("Profile Environment Variable AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY")
            return True

        boto3.setup_default_session(profile_name=aws_profile)
        LOGGER.info("Boto profile : %s", aws_profile)

    def next_token(self, next_request_key_name: str, next_token_key_name: str, extract_key_names: list, function_name,
                   append_reverse=False, append_end_delimiter=None, **kwargs):
        LOGGER.debug("Boto3 API : %s.%s(%s)", self.name, function_name, json.dumps(kwargs))
        response = getattr(self.client, function_name)(**kwargs)
        result_data = response
        for extract_key in extract_key_names:
            result_data = result_data.get(extract_key)
        if not result_data:
            return result_data

        if response.get(next_token_key_name):
            if isinstance(result_data, list) and append_end_delimiter:
                result_data.append(append_end_delimiter + response.get(next_token_key_name) + '\n')
            next_kwargs = kwargs.copy()
            next_kwargs[next_request_key_name] = response.get(next_token_key_name)
            next_result = self.next_token(next_request_key_name, next_token_key_name, extract_key_names, function_name,
                                          append_reverse=append_reverse, append_end_delimiter=append_end_delimiter,
                                          **next_kwargs)
            if isinstance(result_data, list):
                if append_reverse:
                    next_result.extend(result_data)
                    return next_result
                else:
                    result_data.extend(next_result)
                    return result_data
        else:
            return result_data


class S3(Client):
    def __init__(self, **kwargs):
        Client.__init__(self, 's3', **kwargs)

    def get_keys(self, is_sorted=False, sort_reverse=True, **kwargs):
        objects = self.next_token('ContinuationToken', 'NextContinuationToken', ['Contents'], 'list_objects_v2',
                                  **kwargs)
        if not objects:
            return []
        if is_sorted:
            objects = sorted(objects, key=lambda key: key.get('Key'), reverse=sort_reverse)
        return objects

    def read_file(self, **kwargs):
        return self.client.get_object(**kwargs)

    def download(self, download_path, bucket_name, key):
        try:
            save_path = os.path.dirname(download_path)
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            if not os.path.exists(download_path):
                self.client.download_file(bucket_name, key, download_path)
                LOGGER.debug("Download : %s", download_path)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                LOGGER.error("Download file not found : %s/%s", bucket_name, key)
            raise e

    def upload(self, file_path, bucket_name, key):
        self.client.upload_file(file_path, bucket_name, key)
        LOGGER.debug("Upload completed : %s/%s", bucket_name, key)
