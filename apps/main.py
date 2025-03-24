from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
import sqlite3
from datetime import datetime
import os
import time


DATABASE = "database.db"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

from models import User



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

import views,db

@login_manager.user_loader
def load_user(user_id):
    now_users = db.users()
    return now_users.get(int(user_id))

"""
users = {
    1: User(id=1, username='user1', password='password1'),
    2: User(id=2, username='user2', password='password2')
}
"""

if __name__ == '__main__':
    app.run(debug=True)
