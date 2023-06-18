from resources import Class
import random

class Schedule: 
    def __init__(self, data): 
        self.data = data 
        self.classes = [] 
        self.number_of_hard_constraints_violated = 0
        self.number_of_soft_constraints_violated = 0
        self.fitness = -1
        self.number_of_classes = 0
        self.isFitnessChanged = True

    def __str__(self):
        return_string = ""
        for current_class in self.classes:
            return_string += str(current_class) + ", "
        return return_string
        
    def initialize(self):
        current_departments = self.data.get_departments()
        for department in current_departments:
            current_courses = department.get_courses()
            for course in current_courses:
                random_period = self.data.get_periods()[random.randrange(0, len(self.data.get_periods()))]
                
                random_classroom = self.data.get_classrooms()[random.randrange(0, len(self.data.get_classrooms()))]

                random_teacher = course.get_teachers()[random.randrange(0, len(course.get_teachers()))]

                new_class = Class(self.number_of_classes, department, course, random_teacher, random_period, random_classroom)
                
                self.classes.append(new_class)
                self.number_of_classes += 1

        return self

    def get_classes(self):
        self.isFitnessChanged = True
        return self.classes
    
    def get_number_of_hard_constraints_violated(self):
        return self.number_of_hard_constraints_violated
    
    def get_fitness(self):
        if self.isFitnessChanged == True:
            self.fitness = self.calculate_fitness()
            self.isFitnessChanged = False
        return self.fitness
    
    def calculate_fitness(self):
        self.number_of_hard_constraints_violated = 0
        classes = self.get_classes()

        for current_class in classes:
            isEnoughCapacity = current_class.get_classroom().get_capacity() >= current_class.get_course().get_max_students()
            if isEnoughCapacity == False:
                self.number_of_hard_constraints_violated += 1 
            
            for compare_class in classes:
                isSameClass = current_class == compare_class
                isPeriodSame = current_class.get_period() == compare_class.get_period()

                if isSameClass == False and isPeriodSame == True:
                    
                    isClassroomSame = current_class.get_classroom() == compare_class.get_classroom()
                    if isClassroomSame == True:
                        self.number_of_hard_constraints_violated += 1
                    
                    isTeacherSame = current_class.get_teacher() == compare_class.get_teacher()
                    if isTeacherSame == True:
                        self.number_of_hard_constraints_violated += 1
                    
                    isDepartmentSame = current_class.get_department() == compare_class.get_department()
                    if isDepartmentSame == True:
                        self.number_of_soft_constraints_violated += 1
                    
        
        return 1 / ((1.0 * self.number_of_hard_constraints_violated + self.number_of_soft_constraints_violated + 1))

class Population: 
    def __init__(self, size, data): 
        self.size = size
        self.data = data
        self.schedules = []

        for _ in range(0, size):
            self.schedules.append(Schedule(data).initialize())
    
    def get_schedules(self):
        return self.schedules

class Display: 
    def print_data(self, data):
        print("==> All data")
        print("# Number of departments: ", len(data.get_departments()))
        print("# Number of courses: ", len(data.get_courses()))
        print("# Number of teachers: ", len(data.get_teachers()))
        print("# Number of classrooms: ", len(data.get_classrooms()))
        print("# Number of periods: ", len(data.get_periods()))
        print("# Number of classes: ", data.get_number_of_classes())
        print("# Departments: ")
        all_departments = data.get_departments()
        for current_department in all_departments:
            print(f"    {current_department}")
        print("# Courses: ")
        all_courses = data.get_courses()
        for current_course in all_courses:
            print(f"    {current_course}")
        print("# Teachers: ")
        all_teachers = data.get_teachers()
        for current_teacher in all_teachers:
            print(f"    {current_teacher}")
        print("# Classrooms: ")
        all_classrooms = data.get_classrooms()
        for current_classroom in all_classrooms:
            print(f"    {current_classroom}")
        print("# Periods: ")
        all_periods = data.get_periods()
        for current_period in all_periods:
            print(f"    {current_period}")
        print("")

    def print_generation(self, population):
        print("=> Print generation")
        print("    Schedule # | Fitness | # of hard_constraints_violated ")
        schedules = population.get_schedules()
        for index in range(0, len(schedules)):
            schedule = schedules[index]
            print(f"    {index} | {schedule.get_fitness()} | {schedule.get_number_of_hard_constraints_violated()} ")

    def print_schedule(self, schedule, index):
        classes = schedule.get_classes()
        print("    Class # | Department | Course (number of students) | Teacher | Period | Classroom (capacity)")
        for current_class in classes:
            print_statement = f"{current_class.get_id() } | {current_class.get_department().get_name()} | {current_class.get_course().get_name()} ({current_class.get_course().get_max_students()}) | {current_class.get_teacher().get_name()} | {current_class.get_period().get_time()} | {current_class.get_classroom().get_id()} ({current_class.get_classroom().get_capacity()})"
            print(f"    ", print_statement)