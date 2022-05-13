from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField


app = Flask(__name__)
Bootstrap(app)


all_books = [

]


@app.route('/')
def home():
    return render_template("index.html", books=all_books, len=len)


@app.route("/add")
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

