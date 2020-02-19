from flask import *
from flask import request
from models.users import User, db
from flask_login import login_user, current_user


class users:
    def show_login():
        return render_template("users/login.html")

    def login(data):
        try:
            user = User.query.filter_by(
                username=data['username'], password=data['password']).first()
            login_user(user)
            return True
        except Exception as error:
            print(error)
            return {"error": error}

    def registerme(data):
        try:
            newuser = User(
                username=data['username'],
                password=data['password'],
                email=data['email']
            )

            db.session.add(newuser)
            db.session.commit()
            return True
        except Exception as error:
            print(error)
            return {"error": error}
