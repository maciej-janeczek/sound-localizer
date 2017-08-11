from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    N_A = "N/A"


class User(object):
    def __init__(self, name, age, gender):
        if gender not in (Gender.MALE, Gender.FEMALE, Gender.N_A):
            raise ValueError('gender not valid')
        self.gender = gender
        self.name = name
        self.age = age


