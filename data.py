from resources import Course, Department, Teacher, Period, Classroom

CLASSROOMS = [
    {'id': 'CL1', 'capacity': 40},
    {'id': 'CL2', 'capacity': 45},
    {'id': 'CL3', 'capacity': 50},
    {'id': 'CL4', 'capacity': 40},
    {'id': 'CL5', 'capacity': 40},
    {'id': 'CL6', 'capacity': 50},
]

PERIODS = [
    {'id': 'P1', 'time': '8:00 - 9:00'},
    {'id': 'P2', 'time': '9:00 - 10:00'},
    {'id': 'P3', 'time': '10:00 - 11:00'},
    {'id': 'P4', 'time': '11:00 - 12:00'},
    {'id': 'P5', 'time': '12:00 - 13:00'},
]

TEACHERS = [
    {'id': 'T1', 'name': 'Mr. Smith'},
    {'id': 'T2', 'name': 'Ms. Jones'},
    {'id': 'T3', 'name': 'Mr. Davis'},
    {'id': 'T4', 'name': 'Ms. Williams'},
    {'id': 'T5', 'name': 'Mr. Brown'},
    {'id': 'T6', 'name': 'Ms. Miller'},
    {'id': 'T7', 'name': 'Mr. Wilson'},
    {'id': 'T8', 'name': 'Ms. Moore'},
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
            Course('CR1', 'Math', [self.teachers[0], self.teachers[1]], 45, 0),
            Course('CR2', 'Math', [self.teachers[0], self.teachers[1]], 45, 0),
            Course('CR3', 'Biology', [self.teachers[2], self.teachers[3]], 50, 0),
            Course('CR4', 'Physics', [self.teachers[0], self.teachers[1]], 50, 0),
            Course('CR5', 'Chemistry', [self.teachers[2], self.teachers[3]], 40, 0),
            Course('CR6', 'Programming', [self.teachers[0], self.teachers[1]], 45, 0),
            Course('CR7', 'Programming', [self.teachers[0], self.teachers[1]], 45, 0),
            Course('CR8', 'English', [self.teachers[4], self.teachers[5]], 50, 0),
            Course('CR9', 'English', [self.teachers[4], self.teachers[5]], 50, 0),
            Course('CR10', 'History', [self.teachers[6]], 40, 0),
            Course('CR11', 'Translation', [self.teachers[7]], 35, 0),
            Course('CR12', 'Sociology', [self.teachers[6]], 30, 0),
            Course('CR13', 'Literature', [self.teachers[7]], 30, 0),
        ]

        self.departments = [
            Department('D1', 'Engineering', [self.courses[0], self.courses[1], self.courses[2], self.courses[3], self.courses[4], self.courses[5], self.courses[6]]),
            Department('D2', 'English', [self.courses[7], self.courses[8], self.courses[9], self.courses[10], self.courses[11], self.courses[12]]),
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
    

