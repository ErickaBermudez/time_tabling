class Course:
    def __init__(self, id, name, teachers, max_students, min_students):
        self.id = id
        self.name = name
        self.teachers = teachers
        self.max_students = max_students
        self.min_students = min_students
    
    def __str__(self):
        return f"{self.id} {self.name} {self.teachers} {self.max_students} {self.min_students}"
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_teachers(self):
        return self.teachers
    
    def get_max_students(self):
        return self.max_students
    
    def get_min_students(self):
        return self.min_students
    
class Department:
    def __init__(self, id, name, courses):
        self.id = id
        self.name = name
        self.courses = courses
    
    def __str__(self):
        return f"{self.id} {self.name} {self.courses}"
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_courses(self):
        return self.courses
    
class Teacher: 
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __str__(self):
        return f"{self.id} {self.name}"
        
    def get_id(self):
        return self.id
        
    def get_name(self):
        return self.name
        
class Period: 
    def __init__(self, id, time):
        self.id = id
        self.time = time
        
    def __str__(self):
        return f"{self.id} {self.time}"
        
    def get_id(self):
        return self.id
        
    def get_time(self):
        return self.time
        
class Classroom: 
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
    
    def __str__(self):
        return f"{self.id} {self.capacity}"
    
    def get_id(self):
        return self.id
    
    def get_capacity(self):
        return self.capacity
    
class Class: 
    def __init__(self, id, department, course, teacher, period, classroom):
        self.id = id
        self.department = department
        self.course = course
        self.teacher = teacher
        self.period = period
        self.classroom = classroom

    def __str__(self):
        return f"{self.id} {self.department} {self.course} {self.teacher} {self.period} {self.classroom}"
    
    def get_id(self):
        return self.id
    
    def get_department(self):
        return self.department
    
    def get_course(self):
        return self.course
    
    def get_teacher(self):
        return self.teacher
    
    def get_period(self):
        return self.period
    
    def get_classroom(self):
        return self.classroom
    
    def set_teacher(self, teacher):
        self.teacher = teacher

    def set_period(self, period):
        self.period = period

    def set_classroom(self, classroom):
        self.classroom = classroom
