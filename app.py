import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'mcqueen_clinic'
app.config["MONGO_URI"] = 'mongodb+srv://sean:letmeenter@codeinstitute-0x7de.mongodb.net/mcqueen_clinic?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_patients')
def get_patients():
    return render_template('patients.html', patients=mongo.db.patients.find())


@app.route('/add_patient')
def add_patient():
    return render_template('add_patient.html',               doctors=mongo.db.doctors.find())


@app.route('/get_doctors')
def get_doctors():
    return render_template('doctors.html', doctors=mongo.db.doctors.find())


@app.route('/add_doctor')
def add_doctor():
    return render_template('add_doctor.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
