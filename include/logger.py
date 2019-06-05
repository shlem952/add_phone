import datetime

class Logger(object):
    """docstring for Logger."""
    def __init__(self, log_file):
        self.log_file = log_file

    def info(self, string):
        f = open(self.log_file, 'a+')
        f.write(f'[{datetime.datetime.now()}][INFO]{string} \n')
        f.close()

    def error(self, string):
        f = open(self.log_file, 'a+')
        f.write(f'[{datetime.datetime.now()}][ERROR]{string} \n')
        f.close()

    def write(self, string):
        f = open(self.log_file, 'a+')
        f.write(f'[{datetime.datetime.now()}]-{string} \n')
        f.close()


if __name__ == '__main__':
    pass