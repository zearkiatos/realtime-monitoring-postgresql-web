import os
from dotenv import load_dotenv

environment = os.getenv('ENVIRONMENT')

if environment != "local":
    load_dotenv(dotenv_path='.env', override=True)

class Config:
    ENVIRONMENT = environment
    APP_NAME=os.getenv('APP_NAME')
    HOST=os.getenv('HOST')
    DATABASE_HOST=os.getenv('DATABASE_HOST')
    DATABASE_PORT=os.getenv('DATABASE_PORT')
    DATABASE_NAME=os.getenv('DATABASE_NAME')
    DATABASE_USER=os.getenv('DATABASE_USER')
    DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD')