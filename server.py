from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submission', methods=['POST'])
def submission():
	name=request.form['name']
	location=request.form['location']
	favorite=request.form['favorite_language']
	comment=request.form['comment']
	return render_template('results.html', name=name, location=location, favorite=favorite, comment=comment)
app.run(debug=True)
