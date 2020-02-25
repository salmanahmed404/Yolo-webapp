
# Academic Project


### Changing the mysql settings

Go to ``` YoloSite/settings.py ```

In the ```DATABASE``` section:
1. change the ```NAME``` to the desired database name
2. change the ```USER``` to your username in your laptop (or you can create a separate user django to access mySQL)
3. change the ```PASSWORD``` to your mySQL password for that user

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
