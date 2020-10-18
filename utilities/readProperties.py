import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('Common required information', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('Common required information', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Common required information', 'password')
        return password
