import os

class Config:
    API_ID = int( os.getenv("api_id","xxxx") )
    API_HASH = os.getenv("api_hash","53ab7cxxxxxxxxc7bbebxxxx")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1xxxxxx0") )
    CHANNEL_USERNAME = os.getenv("channel_username","testchannel")
    TOKEN = os.getenv("token","xxxxx")
    DOMAIN  = os.getenv("domain","https://testapp.herokuapp.com")