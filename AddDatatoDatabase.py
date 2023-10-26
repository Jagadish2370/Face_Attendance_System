
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://facerecognitionattendenc-d8007-default-rtdb.firebaseio.com/" })

ref = db.reference('Students')

data ={
    "23":
    {
        "name": "Jagadish Dhage",
        "education": "CSE",
        "admission_year": 2020,
        "total_attendance": 1,
        "study_year": 3,
        "gender": "M",
        "last_attendance_time": "2023-03-02 00:54:34"

    },

    "24":
        {
        "name": "Sumit Lomte",
        "education": "CSE",
        "admission_year": 2020,
        "total_attendance": 0,
        "study_year": 3,
        "gender":"M",
        "last_attendance_time": "2023-03-02 00:54:34"

    },
    "69":
        {
        "name": "Menka Shinde",
        "education": "CSE",
        "admission_year": 2020,
        "total_attendance": 0,
        "study_year": 3,
        "gender":"F",
        "last_attendance_time": "2023-03-02 00:54:34"

    },
    "70":
       {
        "name": "Rohini Swami",
        "education": "CSE",
        "admission_year": 2020,
        "total_attendance": 0,
        "study_year": 3,
        "gender":"F",
        "last_attendance_time": "2023-03-02 00:54:34"

    },
}
for key,value in data.items():
    ref.child(key).set(value)
