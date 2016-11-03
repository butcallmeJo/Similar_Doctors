from src.compare import *
from src.define_similarity import *
from src.doctor import Doctor
from create_doctors import *

if __name__ == "__main__":

    doctors = []

    with open('data/doctors.json', 'r') as f:
        try:
            doctors = json.load(f)
        except:
            print "failed to load from json"
            pass

    doc = create_doctor(0)
    similar_doctor = return_similar_doctors(doc, doctors)
