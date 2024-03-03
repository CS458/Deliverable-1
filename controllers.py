from flask import render_template, redirect, request, url_for, session
from settings.app import app, google
from models import User


@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def login_page_post():
    if not request.form["identifier"] or not request.form["password"]:
        error_message = "All the fields are required."

        return render_template("login.html", message=error_message)
    
    user = User(request.form["identifier"])

    if not user.is_valid:
        error_message = "The phone number or email has not a valid format."

        return render_template("login.html", message=error_message)
    
    if user.verify(request.form["password"]):
        session["user_id"] = user.id

        return redirect(url_for("success_page"))
    
    error_message = "Credentials are not correct."

    return render_template("login.html", message=error_message)

@app.route("/google", methods=["POST"])
def login_google():
    return google.authorize(callback=url_for('login_google_authorized', _external=True))
    
@app.route('/google/authorized')
def login_google_authorized():
    resp = google.authorized_response()
    
    if resp is None or resp.get('access_token') is None:
        error_message = "Google authantication failed."

        return render_template("login.html", message=error_message)
    
    session['user_id'] = (resp['access_token'], '')
    
    return redirect(url_for("success_page"))

@app.route("/success")
def success_page():
    if "user_id" in session:
        return render_template("success.html")
    
    return redirect(url_for("logout"))

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "user_id" in session:
        session.pop("user_id")
    
    return redirect(url_for("login_page"))