import os
import time
from . import celery


@celery.task(name='periodic_temporary_file_delete')
def periodic_temporary_file_delete():
    """
    This periodic task is added for removing files from a temporary folder in a scheduled manner.

    :return: None
    """
    print("Celery scheduled task for deleted temporary image files is running")
    path = os.path.join(os.getcwd(), 'temporary_folder')
    print(f"The path in which files will be searched is - {path}")
    deleted_files = 0

    # Delete the files which are older than the specified days
    days = 15
    seconds = time.time() - (days * 24 * 60 * 60)
    file_names = []

    if os.path.exists(path):
        # Get the files only and store in file_names. Avoid sub directories
        for (dir_path, dir_names, filenames) in os.walk(path):
            file_names.extend(filenames)
            break

        for file in file_names[:]:
            file_path = os.path.join(path, file)
            # Delete files with extension .png or .jpg and whose age is more than specified time.
            if seconds >= os.stat(file_path).st_ctime and (file.endswith(".png") or file.endswith(".jpg")):
                print(f"Removing file {file}")
                os.remove(file_path)
                deleted_files += 1

        print(f"Total files deleted due to expiry by the method periodic_temporary_file_delete is - {deleted_files}")
    else:
        print("Path does not exist for temporary file deletion.")


@celery.task(name='sample_background_task')
def sample_background_task():
    """
    Logic for any heavy duty task can be added here
    :return: None
    """
    print("This task runs in background upon api calling")