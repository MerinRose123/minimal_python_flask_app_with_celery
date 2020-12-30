# Minimal Flask App with Celery
This application can be used as a boilerplate for simple flask applications which uses celery.

### Prerequisites
* The redis server should be up and running in port 6379.

* Python should be installed in the system. The application is compatible with python 3.8.5

### Setting up virtual environment

To avoid conflict with the system environment it is recommended to use the application inside a virtual environment.

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

* To start celery along with beat get into file_processing folder in terminal and type 
`celery worker -A app_init.celery --loglevel=INFO -B`