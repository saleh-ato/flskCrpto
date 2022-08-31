from flask import Blueprint, render_template, request, session, redirect
from app import db
from forms.forms import LoginForm
from hashlib import sha256

admin_blueprint = Blueprint('admin_blueprint', __name__)

class Admins(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(10))
    password=db.Column(db.String())
    session=db.Column(db.String())
    
    def verify(self):
        admin = Admins.query.filter_by(username=self.username).first()
        passwd = sha256()
        passwd.update(self.password.encode('utf8'))
        print(admin.password)
        if admin.password == str(passwd.hexdigest()):
            return True
        return False

@admin_blueprint.route("/admin-login")
def Login_view():
    #return "0"
    return render_template("sign-in.html",form=LoginForm())
    # return render_template("auth/sign-in.html",form=signUpForm())
@admin_blueprint.route("/login-handler", methods=['POST'])
def LoginHandler():
    username=request.form.get("username")
    password=request.form.get("passWord")
    # print(username,password)
    # return redirect(request.url_root)
    admin = Admins(username=username, password=password)
    return str(admin.verify())
    return "ok"
#_____________________TEST_________________________
# @admin_blueprint.route('/admin-blue')
# def blueprint():
#     return "This is blueprint app"

@admin_blueprint.route("/admin/show-first-admin")
def show_first_admin():
    admin = Admins.query.first()
    return str(admin.username)+"<br>"+str(admin.password)+"<br>"+str(admin.session)
