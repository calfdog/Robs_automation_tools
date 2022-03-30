# -*- coding: latin-1 -*-
"""
    Description: Some utils for testing
    Developer: Rob Marchetti
"""

import datetime
import random
import string

__author__ = 'Rmarchetti'


class Person():
    first_names = ["James", "Christopher", "Ronald", "Mary", "Lisa", "Michelle", "John", "Daniel", "Anthony", "Patricia", "Nancy", "Laura", "Robert", "Paul", "Kevin", "Linda", "Karen", "Sarah", "Michael", "Mark", "Jason", "Barbara", "Betty", "Kimberly", "William", "Donald", "Jeff", "Elizabeth", "Helen", "Deborah", "David", "George", "Jennifer", "Sandra", "Richard", "Kenneth", "Maria", "Donna", "Charles", "Steven", "Susan", "Carol", "Joseph", "Edward", "Margaret", "Ruth", "Thomas", "Brian", "Dorothy", "Sharon"]
    last_names = ["Smith", "Anderson", "Clark", "Wright", "Mitchell", "Johnson", "Thomas", "Rodriguez", "Lopez", "Perez", "Williams", "Jackson", "Lewis", "Hill", "Roberts", "Jones", "White", "Lee", "Scott", "Turner", "Brown", "Harris", "Walker", "Green", "Phillips", "Davis", "Martin", "Hall", "Adams", "Campbell", "Miller", "Thompson", "Allen", "Baker", "Parker", "Wilson", "Garcia", "Young", "Gonzalez", "Evans", "Moore", "Martinez", "Hernandez", "Nelson", "Edwards", "Taylor", "Robinson", "King", "Carter", "Collins"]
    sex = {"Female": "F", "Male Impersonator": "G", "Male": "M", "Female Impersonator": "N", "Male Name, No Gender Given": "Y", "Female Name, No Gender Given": "Z", "Unknown": "X"}
    rac = {"Asian": "A", "Black": "B", "Native American": "I", "Unknown": "U", "Caucasian/Latino": "W"}
    eye = {"Black": "BLK", "Blue": "BLU", "Brown": "BRO", "Gray": "GRY", "Green": "GRN", "Hazel": "HAZ", "Maroon": "MAR", "Multi Colored": "MUL", "Pink": "PNK", "Unknown": "XXX"}
    hair = {"Bald": "BAL", "Black": "BLK", "Blonde or Strawberry": "BLN", "Brown": "BRO", "Gray or Partially Gray": "GRY", "Red or Auburn": "RED", "Sandy": "SDY", "White": "WHI", "Unknown": "XXX", "Blue": "BLU", "Green": "GRN", "Orange": "ONG", "Pink": "PNK", "Purple": "PLE"}

    def random_sex(self):
        return random.choice([k for k in self.sex for x in self.sex[k]])

    def random_race(self):
        return random.choice([k for k in self.rac for x in self.rac[k]])

    def random_hair(self):
        return random.choice([k for k in self.hair for x in self.hair[k]])

    def random_eyes(self):
        return random.choice([k for k in self.eye for x in self.eye[k]])

    def random_name(self):
        index = random.randint(0, len(self.first_names) - 1)
        return self.first_names[index]

    def random_last_name(self):
        index = random.randint(0, len(self.last_names) - 1)
        return self.last_names[index]

    def random_digits(self, length):
        a = "".join([random.choice(string.digits) for _ in range(length)])
        count = a.count(a)
        count = 0
        while count <= length:
            return ''.join(a)

    def random_string(self, length):
        a = "".join([random.choice(string.ascii_letters) for _ in range(length)])
        a.count(a)
        count = 0
        while count <= length:
            return ''.join(a)

    def date(self):
        today = datetime.date.today()
        day = today.day
        year = today.year
        month = today.month
        return datetime.date(year, month, day)


# # Examples
# util = utilities()
# print("{} {}".format(util.random_name(), util.random_last_name()))
# print(util.random_race())
# print(util.random_sex())
# print(util.random_string(10))
# print(util.random_digits(10))

