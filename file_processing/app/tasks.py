# importing the required modules
import os
import shutil
import time
from . import celery


@celery.task(name='delete_temporary_files_periodically')
def delete_temporary_files_periodically():
    print("Program is running")