import MySQLdb
import hashlib
import radius
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import config

class User(object):
    def __init__(self, username):
        self.username = username


    def add(self, password, level):
        sha1_password = hashlib.md5(password.encode('utf-8'))
        cursor, db = connect_to_db()
        try:
            cursor.execute(f'INSERT INTO users (username, password, level) VALUES ("{self.username}","{sha1_password.hexdigest()}","{level}");')
            db.commit()
            db.close
            return f'User {self.username} successfully added'
        except:
            return f'User {self.username} already exists'
    

    def authenticate(self, password):
        if config.auth_mechanism == 'local':
            sha1_password = hashlib.md5(password.encode('utf-8'))
            cursor, db = connect_to_db()
            cursor.execute(f'SELECT password, level FROM users WHERE username = "{self.username}"')
            if cursor.rowcount == 0:
                return False, 0
            sha1_password_from_db, level = cursor.fetchall()[0]
            print(sha1_password.hexdigest(), sha1_password_from_db)
            db.close
            if sha1_password.hexdigest() == sha1_password_from_db:
                return True, level
            else:
                return False, level
        elif config.auth_mechanism == 'radius':
            r = radius.Radius(config.auth_radius_secret, host=config.auth_radius_server, port=config.auth_radius_port)
            return r.authenticate(self.username, password)
    

    def mod(self):
        pass


def connect_to_db():
    db = MySQLdb.connect(host=config.db_host,
                         user=config.db_user,
                         passwd=config.db_password,
                         db=config.db_name)
    cursor = db.cursor()
    return cursor, db