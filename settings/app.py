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
    consumer_key='your_google_client_id',
    consumer_secret='your_google_client_secret',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)