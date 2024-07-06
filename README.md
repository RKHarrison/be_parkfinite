# BE_PARKFINITE
### PLEASE UPDATE THIS README TO REFLECT CURRENT STATE OF PROJECT BEFORE PUSHING TO GIT

### PROJECT SETUP:
Initiate a virtual environament and reference requirements.txt to install necessary project dependencies:
* Create virtual enivorment in the project root folder (/be_parkfinite):
In your CLI, navigate to the project root folder and run: 
       python3 -m venv venv
* Activate your virtual environment:
In your CLI run:
       source venv/bin/activate
* Install project dependencies:
In your CLI run:
       pip install -r requirements.txt

### RUNNING THE APP:
* Run the app locally on http://127.0.0.1:8000:
In your CLI run:
       uvicorn main:app
* To execute all avaiable test suites:
In your CLI run:
       pytest       
### IF THE APP OR TESTING WONT RUN:
* Ensure your pythonpath is set correctly via an ABSOLTE FILE PATH TO THE PROJECT ROOT FOLDER (/be_parkfinite):
In your CLI run:
        echo $PYTHONPATH
* If there is no set pythonpath then a workaraound is to set it manually: 
        export PYTHONPATH="/path/to/poject/be_parkfinite:$PYTHONPATH"
* To avoid having to run this command every time you activate your venv: 
add a command to the relevant venv/bin/activate file for the operating system you are on.
### AVAILABLE TESTING COMMANDS:
In your CLI:
* To run main api test suite, for main.py endpoints:
       pytest -m main
* To run database utilities test suite:
       pytest -m db_utils
* To run testing utilities test suite:
       use 'pytest -m test_utils' 
### DEVELOPMENT AND PRODUCITON DATABASES:
--PLEASE ADD .ENV FILES TO GIT IGNORE TO KEEP THE DATABASES SECURE!!--
--PLEASE ADD ANY LOCALLY STORED SQLITE DATABASE TO GITIGNORE TOO!--
### Setup .env.development and .env.production in be_parkfinite/api/:
* To create and seed a locally stored SQLite development database add a .env.development file containing the line:
       DATABASE_URL=sqlite:///../dev.db
-Remember to add this file to .gitignore-
* To seed to the hosted production database add a .env.production file containing the following line:
       DATABASE_URL=postgresql://PATH/TO/PRODUCTION/DB/INCLUDING/PASSWORD/
### SEED SPECIFIED DATABASE:
In your CLI run:
       ENV=development python3 seed.py
replace 'development' with 'production' to seed the hosted Postgres production db.

### NOTE: BOTH DATABASES ARE CURRENTLY SEEDED FROM THE SAME DEVELOPMENT DATA FILE!