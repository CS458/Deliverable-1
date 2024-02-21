from settings.app import APP
from flask import render_template


@APP.route('/')
def hello_world():

    return render_template("hello.html")

