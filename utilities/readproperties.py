import configparser
import os.path

config=configparser.RawConfigParser()
config.read('.\\Framework\\Configuration\\config.ini')

class read_config :
    @staticmethod
    def get_app_url():
        url=config.get('common info','base url')
        return url

    @staticmethod
    def get_username():
        uname=config.get('common info','username')
        return uname

    @staticmethod
    def get_password():
        password=config.get('common info', 'password')
        return password
