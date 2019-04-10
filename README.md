
# College DBMS Project


### Changing the mysql settings

Go to ``` YoloSite/settings.py ```

In the ```DATABASE``` section:
	* change the ```NAME``` to the desired database name
	* change the ```USER``` to your username in your laptop (or you can create a separate user django to access mySQL)
	* change the password to your mySQL password for that user

### Creating a working on a virtual environment

Create virtual env
```
virtualenv venv 
```

Activate virtual environemt with

```
. venv/bin/activate
```

Install required dependencies

```
pip3 install -r requirements.txt
```

### IMPORTANT NOTES NOTES

######	Changes made to ```__init__.py``` for mySQL to work on Linux, if it doesnt work on windows, empty the file
######	requirements.txt file updated to just include the required dependencies for this project
######	settings.py added to gitignore so it doesnt mess mySQL everytime theres a commit. Add changes to the bottom of this file, if made to settings.py
