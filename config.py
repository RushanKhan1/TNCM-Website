import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TNCM-Website' # will set an environment variable at time of deployment for better security.
