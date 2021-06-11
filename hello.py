from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length


# create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a key and it is secret"

# Create a Form Class
class NamerForm(FlaskForm):
	name = StringField("What's Your Name?", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a route decorator
@app.route('/')

# def index():
# 	return "<h1>Hello World!</h1>"


def index():
	first_name = "Doug"
	stuff = "This is <strong>bold</strong> text"

	favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms",41]
	return render_template("index.html", 
		first_name = first_name,
		stuff = stuff,
		favorite_pizza = favorite_pizza)

# goes to http://localhost:5000/user/Doug (you have to type in Doug)
@app.route('/user/<name>')
def user(name):
	return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500

# Create name page
@app.route('/name', methods=['GET','POST'])
def name():
	name = None
	form = NamerForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ""
	return render_template("name.html",
		name = name,
		form = form)