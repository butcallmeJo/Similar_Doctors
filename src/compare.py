import json
from src.doctor import Doctor
from src.define_similarity import *
from create_doctors import *

def return_similar_doctors(doctor, doctors):

    data = doctors
    doc = doctor
    ret_doc_list = []

    print "original"
    print doc.get_first_name()
    print doc.get_last_name()
    print doc.get_gender()
    print doc.get_age()
    print doc.get_expertise()
    print doc.get_location()
    print doc.get_review_score()
    print doc.get_languages()

    data = order_location(doc, data)
    data = order_expertise(doc, data)
    data = order_gender(doc, data)
    data = order_languages(doc, data)
    data = order_age(doc, data)
    data = order_scores(data)


    for i in range(min(10, len(data))):
        print "i:", i
        print data[i].get('first_name')
        print data[i].get('last_name')
        print data[i].get('gender')
        print data[i].get('age')
        print data[i].get('expertise')
        print data[i].get('location')
        print data[i].get('review_score')
        print data[i].get('languages')
        ret_doc_list.append(data[i])

    return ret_doc_list
