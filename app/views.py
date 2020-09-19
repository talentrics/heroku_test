from app import app

from flask import render_template, url_for, request, redirect

@app.route("/")
def index():
    return render_template("/public/index.html")


@app.route("/about")
def index():
    return render_template("/public/about.html")

    @app.route("/page3")
def index():
    return render_template("/public/page3.html")
