from resources import Course, Department, Teacher, Period, Classroom, Class

CLASSROOMS = [
    {'id': 'CL1', 'capacity': 20},
    {'id': 'CL2', 'capacity': 20},
    {'id': 'CL3', 'capacity': 25},
    {'id': 'CL4', 'capacity': 40},
]

PERIODS = [
    {'id': 'P0', 'time': '8:00 - 9:00'}, 
    {'id': 'P1', 'time': '9:00 - 10:00'},
    {'id': 'P2', 'time': '10:00 - 11:00'},
    {'id': 'P3', 'time': '11:00 - 12:00'},
    {'id': 'P4', 'time': '12:00 - 13:00'},
]

TEACHERS = [
    {'id': 'T1', 'name': 'Mr. Smith'},
    {'id': 'T2', 'name': 'Ms. Jones'},
    {'id': 'T3', 'name': 'Mr. Davis'},
    {'id': 'T4', 'name': 'Ms. Williams'},
]

class Data: 
    def __init__(self):
        self.classrooms = []
        self.periods = []
        self.teachers = []

        for classroom in CLASSROOMS:
            self.classrooms.append(Classroom(classroom['id'], classroom['capacity']))

        for period in PERIODS:
            self.periods.append(Period(period['id'], period['time']))

        for teacher in TEACHERS:
            self.teachers.append(Teacher(teacher['id'], teacher['name']))
        
        self.courses = [
            Course('CR1', 'Math', [self.teachers[0], self.teachers[1]], 20, 0),
            Course('CR2', 'Science', [self.teachers[1]], 30, 0),
            Course('CR3', 'Physics', [self.teachers[0]], 20, 0),
            Course('CR4', 'English', [self.teachers[2], self.teachers[3]], 25, 0),
            Course('CR5', 'History', [self.teachers[2]], 30, 0),
            Course('CR6', 'Translation', [self.teachers[1]], 20, 0)
        ]

        self.departments = [
            Department('D1', 'Engineering', [self.courses[0], self.courses[1], self.courses[2]]),
            Department('D2', 'English', [self.courses[3], self.courses[4], self.courses[5]]),
        ]

        self.number_of_classes = 0

        for department in self.departments:
            self.number_of_classes += len(department.get_courses())

    def get_classrooms(self):
        return self.classrooms
    
    def get_periods(self):
        return self.periods
    
    def get_teachers(self):
        return self.teachers
    
    def get_courses(self):
        return self.courses
    
    def get_departments(self):
        return self.departments
    
    def get_number_of_classes(self):
        return self.number_of_classes
    

