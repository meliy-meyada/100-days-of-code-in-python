from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import  StringField

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')

app = Flask(__name__)
app.secret_key = "\x06\x9fw\xac>\xff\xe8j\x07\x00\x14\xc6Z\x03\xac\xd2Rv\x9d\x90\x87\x82\xd3\x83'"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)