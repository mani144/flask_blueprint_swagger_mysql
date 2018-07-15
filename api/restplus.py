import logging
import traceback

from flask_restplus import Api
import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='My server API',
          description='simple API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

