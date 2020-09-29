import os
import requests
import boto3
import abc
import logging
import traceback

TARGET_URL = os.environ.get("TARGET_URL")
API_KEY = os.environ.get("API_KEY")

class API_BaseClass(abc.ABC):

    def __init__(self, target_url, api_key):
        self.target_url = target_url
        self.api_key = api_key

    @abc.abstractmethod
    def fetch(self):
        pass

    @abc.abstractmethod
    def make_body(self):
        pass

    def make_header(self, api_key):
        return {
            "headers" : {
                "X-API-KEY" : api_key
            }
        }

class ProfileManager(API_BaseClass):

    def fetch(self):
        pass

    def make_body(self):
        pass

class graphqlManager(API_BaseClass):

    def fetch(self):
        pass

    def make_body(self):
        pass


#TODO: api용 클래스 구현
