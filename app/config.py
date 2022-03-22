import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    DATABASE_URL='postgres://qdyfavlqxncwcc:232ee362c75882e4a1cf39b56e32754a8ae432dd3a4ecbb0d343d21f45b4966f@ec2-3-221-140-141.compute-1.amazonaws.com:5432/db2kjignft16o6'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = './uploads'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    