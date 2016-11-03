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
        if doc.get_location() in area:
            docs_in_area.append(doc)
        else:
            docs_other.append(doc)

    return docs_in_area, docs_other

def order_expertise(doctor, doctors):
    """order doctors by expertise
    doctor: Doctor object - original doctor to get other similar doctor
    doctors: list - list of doctors to order by expertise
    """

    