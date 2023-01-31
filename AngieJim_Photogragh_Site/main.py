# import libraries for server and database mgt
# @your_gardener 05/01/23
import base64
import random
import string
import os
from functools import wraps


from flask import Flask , redirect , render_template , url_for , request , flash, abort
from flask_login import UserMixin , LoginManager, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap

# CREATE FORMS FOR REGISTRATION AND LOGIN
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash , check_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In")

# instantiate the app and setup DB
# from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///images-db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# set CSRF key which is required by flask (I am using a random key) OR PROVIDE BOTH LIKE
SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
app.config.update(dict(
    SECRET_KEY=SECRET_KEY,
    WTF_CSRF_SECRET_KEY=f"crsf_{SECRET_KEY}"
))

db = SQLAlchemy(app)
Bootstrap(app)


##CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False )
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=True)

# images DB  Class
class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    img_name = db.Column(db.String(250))
    img_data = db.Column(db.LargeBinary)

# run once
# db.create_all()
@app.before_first_request
def create_tables():
    db.create_all()

# setup login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # we add query since we are getting it from the db
    return User.query.get(int(user_id))


# all images list
images = []
# error message if file is not found
ERR_NO_FILE_SPECIFIED = 'No file Selected!'

# homepage setup
@app.route('/')
def home():
    image_list = get_images()
    return render_template('home.html', image_list=image_list)

@app.route('/gallery')
def gallery():
    images = get_images()
    image_list = [[],[],[],[],[],[],[]]

    index = 0
    for i in range(len(images)):
        if i%7 != 0:
            image_list[index].append(images[i])
        else:
            index += 1
    return render_template('gallery.html', image_list=images)

@app.route("/pricing")
def pricing():
    return render_template('pricing.html')

# create a random name when uploading the file
def randomstr():
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(15))

# load images from DB
def get_images():
    images = db.session.query(Image).all()
    # if no images in db redirect to add
    if len(images) == 0:
        return render_template('add.html')
    image_list = []
    # read image data from db back to form rendable in html
    for img in images:
        image = base64.b64encode(img.img_data).decode('ascii')
        image_list.append(image)
    return image_list


@app.route('/register', methods = ["GET", "POST"])
def register():
    reg_form = RegisterForm()
    # set max of users to two aka admins
    if len(db.session.query(User).all()) < 3:
        if reg_form.validate_on_submit():
            new_user = User(
                name = reg_form.username.data,
                email = reg_form.email.data,
                password = generate_password_hash(reg_form.password.data,method="pbkdf2:sha256", salt_length=8)
            )
            if User.query.filter_by(email=new_user.email).first():
                flash("Possible Duplicate. Try Logging in")
                return redirect(url_for("login"))
            else:
                db.session.add(new_user)
                db.session.commit()
                flash("Registration Successful")
                # login the newly registered admin
                login_user(new_user)
                return redirect(url_for("add_photo"))
    else:
        flash("Error: Not Allowed! Only page admin(s) are allowed to register")
    return render_template("register.html", form=reg_form)

@app.route('/login', methods=["GET","POST"])
def login():
    if len(db.session.query(User).all()) == 0:
        return redirect(url_for('register'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                login_user(user)
                return redirect(url_for("add_photo"))
            else:
                form.email.data = user.email
                flash("Credentials not accurate!")
        else:
            form.email.data = ""
            flash("Credentials not accurate!")
    return render_template("login.html", form=form)


# decorator function to check if the user is admin
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.is_anonymous:
            return redirect(url_for('login', next=request.url))
        elif current_user.id == 1 or current_user.id == 2:
            return f(*args, **kwargs)
        else:
            return abort(403)

    return decorated_function

@login_required
@admin_only
@app.route("/add", methods=['GET','POST'])
def add_photo():
    image_list = get_images()

    if request.method == 'POST':

        imgfile = request.files['image_url']
        if imgfile.filename == '':
            return ERR_NO_FILE_SPECIFIED

        safefilename = f'{randomstr()}_{imgfile.filename}'
        print(safefilename)
        new_image = Image(
            img_name=safefilename,
            img_data=imgfile.read()
        )
        db.session.add(new_image)
        db.session.commit()

        return redirect(url_for('gallery'))
    return render_template('add.html', image_list=image_list)


# @app.route("/delete/<int:id>",  methods=['post'])
@app.route("/delete/<int:id>", methods=['POST'])
@login_required
@admin_only
def delete(id):
    if request.method == 'POST':
        img_to_del = Image.query.get(id)
        if img_to_del is not None:
            db.session.delete(img_to_del)
            db.session.commit()
            flash("Photo Deleted Successfully!")
        return redirect(url_for('gallery'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    print('Logged out!')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)