import logging.config

import os
from flask import Flask, Blueprint
import settings
from api.restplus import api
from api.auth.endpoints.register import ns as authentication_namespace
from database.models import mysql as db

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)
# mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'jay'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
# app.config['MYSQL_DATABASE_DB'] = 'BucketList'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    #===
    flask_app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    flask_app.config['MYSQL_DATABASE_USER'] = 'root'
    flask_app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
    flask_app.config['MYSQL_DATABASE_DB'] = 'mydatabase'


def initialize_app(flask_app):
    configure_app(flask_app)

    db.init_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(authentication_namespace)
    flask_app.register_blueprint(blueprint)



def main():
    # login_manager.init_app(app)
    print('asasd')
    initialize_app(app)

    log.info('>>>>> Starting development example at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
