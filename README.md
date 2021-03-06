# Minimal Flask App with Celery
This application can be used as a boilerplate for simple flask applications which uses celery. 
The app demonstrates the use of celery for background as well as periodic task running with python flask.

The scheduled task which will be run with the help of celery beat is used to remove image files from 
a specified directory. This helps in deleting temporary files in a periodic manner. The same logic can be used 
to remove log files when they are no longer needed.

### Prerequisites
* The redis server should be up and running in port 6379.

* Python should be installed in the system. The application is compatible with python 3.8.5. 
  Generally python3 would be suitable for the app.

### Setting up virtual environment

To avoid conflict with the system environment it is recommended to use the application inside a virtual environment.
steps:

* Install virtual env with the command `sudo pip3 install virtualenv ` if not already installed.

* Create a virtual env for your app `virtualenv -p python3  venv_name`

* Activate the virtual env with command `source venv_name/bin/activate`
  
* Run the application in virtual env activated terminal.
  
After use, you can deactivate the virtual env using command `deactivate`

### Installing requirements

The requirements for the application can be installed by getting into the folder where requirement.txt resides.

Then type `pip install -r requirements.txt`

### How To Run the App
* To run the application get into the folder file_processing in terminal. Then type `python app_init.py`.

* To start celery along with celery beat get into file_processing folder in terminal and type 
`celery worker -A app_init.celery --loglevel=INFO -B`