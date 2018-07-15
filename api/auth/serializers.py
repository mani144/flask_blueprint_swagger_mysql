from flask_restplus import fields
from api.restplus import api

register_user = api.model('register a user', {
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password'),
    'email': fields.String(required=True, description='email'),
    'firstname': fields.String(required=True, description='first name'),
    'lastname': fields.String(required=True, description='last name'),
})
