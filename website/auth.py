from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.jinja", text="Test")


@auth.route('/logout')
def logout():
    return "<p>Log out<p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.jinja")