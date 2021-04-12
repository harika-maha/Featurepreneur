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

	mycoll.insert_one({'Name':name,"Gender":gender,'Email':email,'Phone':ph_n})
	return render_template("redirect.html", name=name, gender=gender, email=email, ph_n=ph_n)
if __name__=="__main__":
	app.run(debug=True)
