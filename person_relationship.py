# coding=utf-8

class PersonRelationship:
    def __init__(self):
        self.person_relationship = {}

    def insert_data(self, qq_num1, qq_num2):
        self.person_relationship.setdefault((qq_num1, qq_num2), 0)
        self.person_relationship.setdefault((qq_num2, qq_num1), 0)
        self.person_relationship[(qq_num1, qq_num2)] += 2
        self.person_relationship[(qq_num2, qq_num1)] += 1

