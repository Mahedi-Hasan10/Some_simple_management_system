from random import *


class Exam:
    def __init__(self, exam_name):
        self.exam_name = exam_name

    def attend_to_exam(self, subject):
        self.subject = subject
        print(subject)

    def get_marks(self, mark):
        self.mark = mark
        print(mark)
        print('Thank for attending exam')


english = Exam('Mid Term')
english.attend_to_exam('Mathmatics')
english.get_marks(randint(70, 90))

print(english)
