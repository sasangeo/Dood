#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "5456385503:AAHl0cpUACo-rhLwMLgQTDiOK9pJdRYA8JA") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "2515895")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "503118adea978a8d0f82b598558382102515895") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", 1849008944)) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "") # Get from MongoDB Atlas

