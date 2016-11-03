from doctor import Doctor
import operator

"""


define similarity:
    location first,
    similar expertise,
    gender,
    similar languages,
    similar age

    order by review score
"""


def order_location(doctor, doctors):
    """function to order doctors by location
    doctor: Doctor object - original doctor to get other similar doctor
    doctors: list - list of doctors to order by location
    """

    bay_area = [
        "San Francisco", "San Mateo", "Oakland", "Berkeley"
    ]

    la_area = [
        "Los Angeles", "Irvine", "Santa Monica"
    ]

    docs_in_area = []
    docs_other = []

    location = doctor.get_location()
    if location in bay_area:
        area = bay_area
    else:
        area = la_area

    for doc in doctors:
        if doc.get('location') in area:
            docs_in_area.append(doc)
        else:
            docs_other.append(doc)

    return docs_in_area

def order_expertise(doctor, doctors):
    """order doctors by expertise
    doctor: Doctor object - original doctor to get other similar doctor
    doctors: list - list of doctors to order by expertise
    """

    trimmed_doc_list = []

    for doc in doctors:
        if doc.get('expertise') == doctor.get_expertise():
            trimmed_doc_list.append(doc)

    return trimmed_doc_list

def order_gender(doctor, doctors):
    """order doctors by gender
    doctor: Doctor object - original doctor to get other similar doctor
    doctors: list - list of doctors to order by gender
    """

    trimmed_doc_list = []

    for doc in doctors:
        if doc.get('gender') == doctor.get_gender():
            trimmed_doc_list.append(doc)

    return trimmed_doc_list

def order_age(doctor, doctors):
    """order doctors by age
    doctor: Doctor object - original doctor to get other similar doctor
    doctors: list - list of doctors to order by age
    """

    trimmed_doc_list = []
    age_range_min = doctor.get_age()-10
    age_range_max = doctor.get_age()+10

    for doc in doctors:
        if age_range_min <= doc.get('age') <= age_range_max:
            trimmed_doc_list.append(doc)

    return trimmed_doc_list

def order_languages(doctor, doctors):
    """order doctors by languages
    doctor: Doctor object - original doctor to get other similar doctor
    doctors: list - list of doctors to order by languages
    """

    doctor_lang = doctor.get_languages()
    trimmed_doc_list = []

    for doc in doctors:
        curr_doc_lang = doc.get('languages')
        for lang in curr_doc_lang:
            if lang in doctor_lang:
                trimmed_doc_list.append(doc)

    return trimmed_doc_list

def order_scores(doctors):
    """order doctors by score
    doctor: Doctor object - original doctor to get other similar doctor
    doctors: list - list of doctors to order by age
    """

    # return doctors.sort(key=operator.methodcaller('get_review_score'))
    # print doctors
    print
    print
    ret_docs = sorted(doctors, key=operator.itemgetter('review_score'), reverse=True)
    # ret_docs = doctors.sort(key=lambda k: k['review_score'])
    # print ret_docs
    return ret_docs
