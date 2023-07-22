

from flask import Flask, url_for, render_template, redirect, flash, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passwd123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class user(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, email, password):
        self.email = email
        self.password = password

# login primary op
@app.route('/', methods=['POST','GET'])
def login():
    # if reques.method == 
    if request.method == 'POST':
        email = request.get('email')
        password = request.get('password')
        session['email'] = email
        session['password'] = password
        return redirect(url_for(''))
    else:
        # if SystemError
        return render_template('login.html')

# sign up secondary op
@app.route('/signup', methods=['POST', 'GET'])
def sign_up():
    return render_template('sign_up.html')


@app.route('/home')
def home():
    return "<h1>Successfully login!</h1>"

@app.route('/check_account')
def check_account():
    

@app.route('/logout')
def logout():
    return "<h>Logout!</h"


if __name__=='__main__':
    app.run(debug=True)