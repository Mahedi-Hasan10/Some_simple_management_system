class Student:
    def __init__(self, name, cur_class, id):
        self.name = name
        self.cur_class = cur_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student : {self.name}, Class : {self.cur_class}, Id : {self.id}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher : {self.name}, Subject : {self.subject}, id : {self.id}'


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers)+100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, payment):
        if payment < 6500:
            print(
                f'You cannot enroll under 6500 taka and you need {6500-payment} taka more to enroll')
        else:
            id = len(self.students)+1
            student = Student(name, 'C', id)
            self.students.append(student)
            print(f'Enrolled succesfull, extra money {payment-6500}')

    def __repr__(self) -> str:
        print(f'Welcome to ', self.name)
        print("--------Our Teachers-------------")
        for teacher in self.teachers:
            print(teacher)
        print("--------Our Students-------------")
        for student in self.students:
            print(student)
        return f'Thank you'


phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)
