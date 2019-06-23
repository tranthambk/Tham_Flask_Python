from dateTime import DateTime
from flask import Flask, render_template,url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='19cc9b894b476df78ed08984fe77bc6a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20),unique=True, nullable=False)
	username = db.Column(db.String(120),unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60),nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"
class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.column(db.String(100), nullable=False)
	data_posted= db.Column(db.DateTime,nullable=False, default=dateTime.utcnow)
	content = db.Column(db.Text, nullable=False)

	def _repr_(self):
posts = [
	{
		'author': 'tran thi tham',
		'title': 'Blog Post 1',
		'content': 'First content',
		'date_posted': 'April 21, 2018'
	},
	{
		'author': 'tran thi truc',
		'title': 'Blog Post 2',
		'content': 'Second content',
		'date_posted': 'April 22, 2018'
	}
]
@app.route("/")
@app.route("/home")
def 	hello():
	return render_template('home.html',posts=posts)
@app.route("/about")
def 	about():
	return render_template('about.html',title='about')
@app.route("/register",methods=['GET','POST'])
def 	register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success!')
		return redirect(url_for('hello'))
	return render_template('register.html',title='Register',form=form)
@app.route("/login",methods=['GET','POST'])
def 	login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data =='admin@gmail.com' and form.password.data=='password':
			flash('You have been logged in!','success')
			return redirect(url_for('hello'))
		else:
			flash('Login Unsuccessful. Please check again','danger')
	return render_template('login.html',title='Login',form=form)

	if __name__=='__main__':
		app.run(debug=True)