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

    def get_profile(self):
        return {
            "device_id" : "kimsehwan",
            "Fields" : [
                "rpm",
                "speed",
                "brake",
                "oilTemp",
                "oilStatus"
             ]
        }

        #TODO: 추후에 실제 dynamoDB에 있는 값을 땡겨올것..

class graphqlManager(API_BaseClass):

    def fetch(self):
        pass

    def make_body(self):
        pass


#TODO: api용 클래스 구현
