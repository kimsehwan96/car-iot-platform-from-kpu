import os
import datetime
import time
import boto3


def hanlder(event, context):
    print("this lambda has been invoked !")
    print(event)

    