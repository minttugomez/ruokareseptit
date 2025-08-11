from flask import Flask, render_template, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from repositories.user_repository import create_user, get_password_hash
import sqlite3
import config

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "ERROR: passwords do not match"
    password_hash = generate_password_hash(password1)

    try:
        create_user(username, password_hash)
    except sqlite3.IntegrityError:
        return "ERROR: username is not available"

    return "Registration complete"

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    password_hash = get_password_hash(username)

    if check_password_hash(password_hash, password):
        session["username"] = username
        return redirect("/")
    else:
        return "ERROR: wrong username or password"

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
