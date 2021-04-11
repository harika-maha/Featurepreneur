from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
import pymongo

mongo_uri = "mongodb://localhost:27017/"
client = pymongo.MongoClient(mongo_uri)
mydb = client.formDB
mycoll = mydb.people
app = Flask(__name__)
@app.route('/')

def form():
	return render_template("form.html")

@app.route('/form', methods=["POST"])
def redirect():
	name = request.form.get("Name")
	gender = request.form.get("Gender")
	email = request.form.get("email")
	ph_n = request.form.get("pno")
	mongo.db.users.insert({'Name':request.form.get('Name'),'Gender':request.form.get("Gender"),'email':request.form.get('email'),'pno':request.form.get('pno')})
	return render_template("redirect.html")
