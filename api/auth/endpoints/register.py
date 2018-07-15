import logging

from flask_restplus import Resource
from flask import Response, redirect, request, session, abort
from api.auth.serializers import register_user
from api.auth.database_calls import create_user

from api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('auth', description='auth')


@ns.route('/register')
class Register(Resource):
    @api.expect(register_user)
    def post(self):
        """
        Creates a new user.
        """
        data = request.json
        create_user(data)
        return None
