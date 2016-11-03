from src.doctor import Doctor
import json
import random

def rand_fname(gender):
    if gender == "male":
        names = [
        "Noah", "Liam", "Mason", "Jacob", "William", "Ethan", "James", "Alexander", "Michael", "Benjamin"
        ]
    else:
        names = [
            "Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia", "Abigail", "Emily", "Charlotte", "Harper"
        ]
    return random.choice(names)

def rand_lname():
    names = [
        "Smith", "Johnson", "Gaillard", "Chu", "Suh", "Lee", "Perrey", "Perry", "Britton", "Burton", "Jones", "Williams", "Desmole", "Jackson", "Moore", "Clinton", "Trump", "Barbier", "Kalache"
    ]
    return random.choice(names)

def rand_gender():
    gender = ["male", "female"]
    return random.choice(gender)

def rand_age():
    return random.randint(22, 77)

def rand_expertise():
    expertises = [
        "Oncology", "Radiology", "Cardiology", "Gastroenterology", "Gynecology", "Maternity", "Microbiology", "Nephrology", "Neurology"
    ]
    return random.choice(expertises)

def rand_location():
    locations = [
        "San Francisco", "San Mateo", "Oakland", "Los Angeles", "Irvine", "Santa Monica", "Berkeley"
    ]
    return random.choice(locations)

def rand_scores():
    scores = []
    for i in range(10):
        scores.append(round(random.uniform(1, 5)*2)/2)
    return scores

def rand_languages():
    languages = [
        "French", "Spanish", "Mandarin", "Cantonese", "Korean", "Japanese", "German", "Italian", "Russian"
    ]
    ret_langs = ["English"]
    for i in range(random.randint(1, 5)):
        lang = random.choice(languages)
        if lang not in ret_langs:
            ret_langs.append(lang)
    return ret_langs

def create_doctor(i):
    gender = rand_gender()
    doc = Doctor(
        i,
        rand_fname(gender),
        rand_lname(),
        gender,
        rand_age(),
        rand_expertise(),
        rand_location(),
        rand_scores(),
        rand_languages()
    )
    return doc

if __name__ == "__main__":

    data = []

    with open('data/doctors.json', 'r') as f:
        try:
            data = json.load(f)
        except:
            pass

    for i in xrange(500):
        doc = create_doctor(i)
        data.append(doc.get_dictionary())

    with open('data/doctors.json', 'w') as f:
        print "writing to file"
        json.dump(data, f)
