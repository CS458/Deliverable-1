import os
from flask import Flask
from settings.config import TEMPLATE_DIR, STATIC_DIR
from flask_oauthlib.client import OAuth


app = Flask(
    __name__, 
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

app.secret_key = 'super secret key'

oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key='333000672057-0fht742i8jn33po9c4nthj6lhovhpr3d.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)