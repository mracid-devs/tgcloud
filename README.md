
![Logo](https://i.postimg.cc/J0XSxqqM/TGCLOUD.png)


# TGCLOUD 🪁

+ Simple telegram bot to convert files into direct download link.you can use telegram as a file server 🪁

## Features

- Easy to Deploy
- Heroku Supported
- Quick Download Links


## Deployment

* Docker :

    > install docker , docker-compose
    
    > set Environment or edit Config/__init__.py
    
    `docker-compose up`

* Heroku :

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/mracid-devs/tgcloud)

    `git clone https://github.com/mracid-devs/tgcloud`
    
    > edit Config/__init__.py
    
    `heroku create` or `heroku git:remote -a appname`
    
    `git push heroku master`

* Cli :

    > install python3.8+
    
    `git clone https://github.com/mracid-devs/tgcloud`
    
    > set Environment or edit Config/__init__.py
    
    `pip install -r requirements.txt`
    
    run web : 
        `gunicorn main:main --workers 4 --threads 4 --bind 0.0.0.0:$PORT --timeout 86400 --worker-class aiohttp.GunicornWebWorker`
        
    run bot :
        `python -m bot`
        
    run web and bot :
        `./start`

