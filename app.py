import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'mcqueen_clinic'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_patients')
def get_patients():
    return render_template('patients.html', patients=mongo.db.patients.find())


@app.route('/search_patient', methods=['POST'])
def search_patient():
    search_type = request.form.get("search_type")
    print(search_type)
    search_query = request.form.get("search_query")
    print(search_query)
    search_results = mongo.db.patients.find({search_type: search_query})
    print(search_results)
    return render_template('patients.html', patients=search_results)


@app.route('/add_patient')
def add_patient():
    return render_template('add_patient.html', doctors=mongo.db.doctors.find())


@app.route('/insert_patient', methods=['POST'])
def insert_patient():
    patients = mongo.db.patients
    patients.insert_one(request.form.to_dict())
    return redirect(url_for('get_patients'))


@app.route('/edit_patient/<patient_id>')
def edit_patient(patient_id):
    the_patient = mongo.db.patients.find_one({"_id": ObjectId(patient_id)})
    all_doctors = mongo.db.doctors.find()
    return render_template('edit_patient.html', patient=the_patient, doctors=all_doctors)


@app.route('/update_patient/<patient_id>', methods=["POST"])
def update_patient(patient_id):
    patients = mongo.db.patients
    patients.update({'_id': ObjectId(patient_id)},
    {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'card_num': request.form.get('card_num'),
        'phone': request.form.get('phone'),
        'email': request.form.get('email'),
        'address': request.form.get('address'),
        'city': request.form.get('city'),
        'postal_code': request.form.get('postal_code'),
        'doctor': request.form.get('doctor')
    })
    return redirect(url_for('get_patients'))


@app.route('/delete_patient/<patient_id>')
def delete_patient(patient_id):
    mongo.db.patients.remove({'_id': ObjectId(patient_id)})
    return redirect(url_for('get_patients'))


@app.route('/get_doctors')
def get_doctors():
    return render_template('doctors.html', doctors=mongo.db.doctors.find())


@app.route('/insert_doctor', methods=['POST'])
def insert_doctor():
    doctors = mongo.db.doctors
    doctors.insert_one(request.form.to_dict())
    return redirect(url_for('get_doctors'))


@app.route('/delete_doctor/<doctor_id>')
def delete_doctor(doctor_id):
    mongo.db.doctors.remove({'_id': ObjectId(doctor_id)})
    return redirect(url_for('get_doctors'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
