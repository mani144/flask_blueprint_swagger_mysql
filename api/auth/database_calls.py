from database.models import mysql
from werkzeug import generate_password_hash, check_password_hash

import json

def create_user(data):
    _username = data.get('username')
    _password = data.get('password')
    _email = data.get('email')
    _firstname = data.get('firstname')
    _lastname = data.get('lastname')
    conn = mysql.connect()
    cursor = conn.cursor()
    _hashed_password = generate_password_hash(_password)
    cursor.callproc('sp_createUser', (_firstname,_lastname,_username, _email, _hashed_password))
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        return json.dumps({'message': 'User created successfully !'})
    else:
        return json.dumps({'error': str(data[0])})
