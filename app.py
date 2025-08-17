from flask import Flask, render_template, request, session, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from repositories.user_repository import create_user, get_password_hash
from repositories.recipe_repository import get_all_recipes, add_new_recipe
import sqlite3
import config

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    if "username" not in session:
        return redirect("/login")
    recipes = get_all_recipes() or []
    return render_template("index.html", recipes=recipes)

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/newrecipe")
def new_recipe():
    if "username" not in session:
        return redirect("/login")
    return render_template("new_recipe.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if len(username) < 4:
        flash("ERROR: username must be at least 4 characters")
        return redirect("/register")
    if len(password1) < 8:
        flash("ERROR: password must be at least 8 characters")
        return redirect("/register")
    if password1 != password2:
        flash("ERROR: passwords do not match")
        return redirect("/register")
    password_hash = generate_password_hash(password1)

    try:
        create_user(username, password_hash)
    except sqlite3.IntegrityError:
        flash("ERROR: username is not available")
        return redirect("/register")

    flash("Registration successful. You may now log in.")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    password_hash = get_password_hash(username)

    if password_hash is not None and check_password_hash(password_hash, password):
        session["username"] = username
        return redirect("/")
    else:
        flash("ERROR: wrong username or password")
        return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/recipes/create", methods=["POST"])
def create_recipe():
    if "username" not in session:
        return redirect("/login")

    user_id = session.get("user_id")
    title = request.form["title"]
    description = request.form["description"]
    ingredients = request.form["ingredients"]
    instructions = request.form["instructions"]

    if not user_id:
        flash("User not recognized. Please log in again.")
        return redirect("/login")

    add_new_recipe(user_id, title, description, ingredients, instructions)
    flash("Recipe added successfully!")
    return redirect("/")
