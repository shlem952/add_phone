from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import MySQLdb

from include.cucm_axl import connect_to_cucm
from include.user_auth import User

import config

def connect_to_db():
    db = MySQLdb.connect(host=config.db_host,
                         user=config.db_user,
                         passwd=config.db_password,
                         db=config.db_name)
    cursor = db.cursor()
    return cursor, db

app = Flask(__name__)
app.secret_key = os.urandom(12)

text_fields = {'1':{'name':'Модель телефона','var':'phone_model', 'data_validate':'', 'type':'list', 'values':['7841','7821','7811','7954','8888']},
               '2':{'name':'Мак адреса телефона','var':'telephone_mac', 'data_validate':'Например: C444A0759B88', 'type':'text'},
               '3':{'name':'ФИО Англ','var':'full_name', 'data_validate':'Например: Ivanov Ivan', 'type':'text'},
               '4':{'name':'ФИО Рус','var':'full_name_ru', 'data_validate':'Например: Иванов Иван', 'type':'text'},
               '5':{'name':'Username','var':'user_id', 'data_validate':'Например: i.ivanov', 'type':'text'},
               '6':{'name':'Номер телефона','var':'directory_number', 'data_validate':'Например: 8888', 'type':'text'},
               '7':{'name':'Мобльный номер','var':'directory_number_mob', 'data_validate':'Например: 89999999999', 'type':'text'},
               '8':{'name':'Компания','var':'company', 'data_validate':'', 'type':'list', 'values':['TKCenter','8News','Stoloto','test']}}

telephone_type = ['7841','7821','7811','7954']
companys = ['TKCenter','8News','Stoloto']

@app.route("/")
def index():
    data = {}
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html' , data=data, 
                                              telephone_type=telephone_type, 
                                              companys=companys, 
                                              text_fields=text_fields)

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    session['username'] = username
    user = User(username)
    auth_status, level = user.authenticate(password)
    if auth_status == True:
        session['logged_in'] = True
    else:
        flash('Неверный пароль!')
    return redirect('/')

@app.route('/phone_registration', methods=['POST'])
def phone_registration():
    if not session.get('logged_in'):
        return render_template('login.html')
    check_fields, data, error = data_check(request.form)
    if not check_fields:
        return render_template('index.html' , data=data, 
                                        telephone_type=telephone_type, 
                                        companys=companys, 
                                        text_fields=text_fields,
                                        error = error)
    else:
        status = create_phone(data)
        return status


def data_check(data):
    print(data)
    return True, 'True', 'True'

def create_phone(data):
    print(data)
    return True


if __name__ == "__main__":
    app.run()
