import math
import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob 
        self.__marks = {}
        self.__gpa = 0.0

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_marks(self):
        return self.__marks
    def get_gpa(self):
        return self.__gpa
    
    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def calculate_gpa(self, course):
        marks_list = []
        credits_list = []
        for c in course:
            c_id = c.get_id()
            if c_id in self.__marks:
                marks_list.append(self.__marks[c_id])
                credits_list.append(c.get_credits())
        
        if not credits_list:
            self.__gpa = 0.0
            return self.__gpa

        np_marks = np.array(marks_list, dtype=float)
        np_credits = np.array(credits_list, dtype=float)

        total_credits = np.sum(np_credits)
        if total_credits == 0:
            self.__gpa = 0.0
        else:
            self.__gpa = np.sum(np_marks * np_credits) / total_credits
            
        return self.__gpa

def round_down(score):
    return math.floor(score * 10) / 10.0