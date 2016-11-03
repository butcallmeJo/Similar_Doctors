"""
doctor.py



"""


class Doctor(object):
    """A Doctor

    Attributes:
        first_name
        last_name
        gender
        age
        expertise
        location
        review_score
        languages
    """

    def __init__(self, id, first_name, last_name, gender, age, expertise, location, review_scores, languages):
        """Return a new Doctor object"""

        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age
        self.__expertise = expertise
        self.__location = location
        self.__review_scores = review_scores
        self.__languages = languages

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def get_expertise(self):
        return self.__expertise

    def get_location(self):
        return self.__location

    def get_review_score(self):
        # TODO write logic to calculate score
        return self.__review_scores

    def get_languages(self):
        return self.__languages

    def get_dictionary(self):
        return {
            'id': self.__id,
            'first_name': self.__first_name,
            'last_name': self.__last_name,
            'gender': self.__gender,
            'age': self.__age,
            'expertise': self.__expertise,
            'location': self.__location,
            'review_score': self.__review_scores,
            'languages': self.__languages
        }
