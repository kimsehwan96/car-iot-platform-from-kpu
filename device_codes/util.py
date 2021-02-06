import json
import os

PROFILE_NAME = 'profile.json'
CUR_DIR = os.path.dirname(__file__)
LOCAL_PROFILE_PATH = os.path.join(CUR_DIR, PROFILE_NAME)


class Profile:
    def __init__(self, filepath: str = None):  # default path is local path
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = LOCAL_PROFILE_PATH

        self.profile = self.__set_profile()  # get profile from json

    def __set_profile(self):
        try:
            with open(self.filepath, 'r') as f:
                profile = json.load(f)
                return profile
        except Exception as e:  # TODO: check error cases we should handle
            print("error occured")
            return None

    def get_data_types(self):
        return self.profile.get('dataTypes')

    def get_device_id(self) -> str:
        return self.profile.get('deviceId')

# TODO: How to get this profiles without making instance of Profile?
