import json

DATA_SOURCE = """{
    "deviceId" : "sehwan",
    "carType" : "K3",
    "dataTypes" : [
        "ENGINE_LOAD",
        "ENGINE_RPM",
        "VEHICLE_SPEED",
        "THROTTLE"
    ]
}"""

class ProfileManager:
    def __init__(self, path=None) -> None:
        self.path = path

    def __open_json(self, path) -> dict:
        pass

    def get_profile(self) -> dict:
        if self.path:
            return self.__open_json(self.path)
        else:
            return json.loads(DATA_SOURCE)
