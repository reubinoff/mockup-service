from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import flask_restful

app = Flask(__name__)
original_flask_handle_exception = app.handle_exception
original_flask_handle_user_exception = app.handle_user_exception
api = flask_restful.Api(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

# modifies flask handle exception default behavior, but is implemented badly.
# api = flask_restful.Api(app)
#
# # so we restore flask default error handling behavior
app.handle_exception = original_flask_handle_exception
app.handle_user_exception = original_flask_handle_user_exception
