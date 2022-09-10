from flask import Blueprint, render_template, request, session, redirect, url_for
from app import db
from forms.forms import LoginForm
from hashlib import sha256

admin_blueprint = Blueprint('admin_blueprint', __name__)

class Admins(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(10), unique=True)
    password=db.Column(db.String())
    session=db.Column(db.String())
    
    def verify(self):
        admin = Admins.query.filter_by(username=self.username).first()
        passwd = sha256()
        passwd.update(self.password.encode('utf8'))
        # print(admin.password)
        if admin.password == str(passwd.hexdigest()):
            return True
        return False
    
def isAdmin(username_session, password_session, role_session):
    # username = session["username_session"]
    # print(username_session)
    # return ""
    # print(user.username)
    # print(user.password)
    # print(password_session)
    # print(password_session)
    try:
        user = Admins.query.filter_by(username=username_session).first()
        passwd = sha256()
        passwd.update(password_session.encode('utf8'))
        hashed_session = passwd.hexdigest()
        # print(str(passwd.hexdigest()))
        #this if is ok?
        if user.password == hashed_session and (session["role"]==session["username"]+session["password"]):
            return True
        return False
    except Exception as e:
        return False

@admin_blueprint.route("/admin-login")
def Login_view():
    return render_template("sign-in.html",form=LoginForm())

@admin_blueprint.route("/login-handler", methods=['POST'])
def LoginHandler():
    username=request.form.get("username")
    password=request.form.get("passWord")
    # print(username,password)
    # return redirect(request.url_root)
    admin = Admins(username=username, password=password)
    if admin.verify():
        # print("noice!")
        session["username"]=admin.username
        session["password"]=admin.password
        session["role"]=session["username"]+session["password"]
        # session["role"]=request.cookies.get("session")
        # print(session["role"])
        return redirect("/admin-dashboard")
    print(str(admin.verify()))
    return redirect("/")

@admin_blueprint.route("/admin-dashboard")
def Dashboard():
    is_admin = False
    try:
        is_admin = isAdmin(session["username"], session["password"], session["role"])
    except Exception:
        pass
    if is_admin:
        return render_template("admin/dashboard.html")
    else:
        return redirect(url_for('admin_blueprint.Login_view'))

#_____________________TEST_________________________
# @admin_blueprint.route('/admin-blue')
# def blueprint():
#     return "This is blueprint app"

@admin_blueprint.route("/admin/show-first-admin")
def show_first_admin():
    admin = Admins.query.first()
    return str(admin.username)+"<br>"+str(admin.password)+"<br>"+str(admin.session)
