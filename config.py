import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'c8199c7eb5fd5b82690a584aaacb683b9c45af96'