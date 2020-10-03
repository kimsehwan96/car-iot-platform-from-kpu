import os
import datetime
import time
import boto3


def handler(event, context):
    print("this lambda has been invoked !")
    print(event)

    