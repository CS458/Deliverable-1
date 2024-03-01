from flask import render_template, redirect, request, url_for, session
from settings.app import app
from models import User


@app.route("/", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def login_page_post():
    if not request.form["identifier"] or not request.form["password"]:
        error_message = "All the fields are required."

        return render_template("login.html", message=error_message)
    
    user_service = User(request.form["identifier"])

    if not user_service.is_valid:
        error_message = "The phone number or email has not a valid format."

        return render_template("login.html", message=error_message)
    
    if user_service.verify(request.form["password"]):
        session["user_id"] = user_service

        return redirect(url_for("success"))
    
    error_message = "Credentials are not correct."

    return render_template("login.html", message=error_message)
    
@app.route("/success")
def success_page():
    if "user_id" in session:
        return render_template("success.html")
    
    return redirect(url_for("logout"))

@app.route("/logout")
def logout():
    if "user_id" in session:
        session.pop("user_id")
    
    return render_template("logout.html")