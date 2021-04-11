from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']= 'mongodb://localhost:27017/'
mongo=PyMongo(app)
@app.route('/')

def form():
	return render_template("form.html")

@app.route('/form', methods=["POST"])
def redirect():
	if 'Name' in request.files:
		name = request.files['Name']
		mongo.db.users.insert({'Name':request.form.get('Name'),'Gender':request.form.get("Gender"),'email':request.form.get('email'),'pno':request.form.get('pno')})
	return render_template("redirect.html")
