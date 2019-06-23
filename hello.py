from flask import Flask, render_template,url_for,flash, redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='19cc9b894b476df78ed08984fe77bc6a'
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