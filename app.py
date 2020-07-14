from flask import Flask, render_template, redirect, url_for,request,Response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,FileField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app=Flask(__name__,static_url_path='/static')
app.config['SECRET_KEY'] = 'TNCM-Website'

@app.route("/",methods=['GET', 'POST'])
def index():
    return "<center><h1>Start Building This Website !"

if __name__=="__main__":
    app.run(debug=True)
