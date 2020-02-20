from flask import *
from flask import request
from controllers.blog import blog as theblog
from models.init import db
# from models.users import User,db
from models.blog import Postes
from models.users import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from controllers.users import users as theuser
from flask import Flask, flash, request, redirect, url_for



app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'

app.config['SECRET_KEY'] = 'anyrandomstring'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/shahriar/Projects/blogflask/photoshooter.db'
db.init_app(app)

with app.app_context():
    db.create_all()

# مدیریت ورود و خروج ها با این متغییر انجام میشود
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

# نمایش صفحه ایندکس بلاگ
@app.route("/")
@login_required
def home():
    return theblog.show_index()


@app.route("/login/")
def login():
    return theuser.show_login()


@app.route("/loginme", methods=['POST'])
def loginme():
    data = request.form.to_dict()
    if theuser.login(data) == True:
        return redirect('/')
    else:
        return redirect('/login')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

@app.route("/test/")
def test():
    return render_template('text.html')


@app.route("/register/")
def register():
    return render_template('users/register.html')

@app.route("/registerme", methods=['POST'])
def registerme():
    data = request.form.to_dict()
    if theuser.registerme(data) == True:
        return redirect('/')
    else:
        return redirect('/login')


@app.route('/upload_file', methods=['GET', 'POST'])
@login_required
def upload_file():
    if theblog.newpost(request, app) == True :
        return redirect('/')


@app.route('/updatepost', methods=['GET', 'POST'])
@login_required
def updatepost():
    if theblog.updatepost(request, app) == True:
        return redirect('/')


@app.route('/deletepost/<id>', methods=['GET'])
@login_required
def deletepost(id):
    if theblog.deletepost(id=id,username=current_user.username) == True:
        return redirect('/')

if __name__ == "__main__":
    app.run()
