import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

print(config['DB']['Host'])
print(config['DB']['Port'])
print(config['DB']['User'])
print(config['DB']['Passwd'])
