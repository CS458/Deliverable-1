import os
from flask import Flask
from settings.config import TEMPLATE_DIR


APP = Flask(
    __name__, 
    template_folder=TEMPLATE_DIR,
)
