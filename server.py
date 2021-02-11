from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# @app.route('/<int:width>')
# @app.route('/<int:width>/<int:height>')
# def play(width=8, height=8, color1='red', color2='black'):
def showUsers():
	users = [
		{'first_name': 'Michael', 'last_name': 'Choi'},
		{'first_name': 'John', 'last_name': 'Supsupin'},
		{'first_name': 'Mark', 'last_name': 'Guillen'},
		{'first_name': 'KB', 'last_name': 'Tonel'}
	]
	num_users = len(users)
	print(users)
	print(num_users)
	title = "Users List"
	return render_template('index.html', title=title, users=users, num_users=num_users)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('index.html', title='404', phrase='Sorry! No response. Try again.', num_times=1)

if __name__ == "__main__":
	app.run(debug=True)