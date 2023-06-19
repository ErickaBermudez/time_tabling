import settings
import random
from classScheduling import Population, Schedule

class GeneticAlgorithm: 
    def __init__(self, data):
        self.data = data
    def evolve(self, population):
        return self.mutate_population(self.crossover_population(population))
    
    def crossover_population(self, population):
        current_population = Population(0, self.data)
        for i in range(settings.ELITISM_COUNT):
            current_population.get_schedules().append(population.get_schedules()[i])
        i = settings.ELITISM_COUNT
        while i < settings.POPULATION_SIZE:
            schedule_1 = self.select_tournament_population(population).get_schedules()[0]
            schedule_2 = self.select_tournament_population(population).get_schedules()[0]
            current_population.get_schedules().append(self.crossover_schedule(schedule_1, schedule_2))
            i += 1
        return current_population
    
    def select_tournament_population(self, population):
        tournament_population = Population(0, self.data)
        i = 0
        while i < settings.TOURNAMENT_SELECTION_SIZE:
            tournament_population.get_schedules().append(population.get_schedules()[random.randrange(0, settings.POPULATION_SIZE)])
            i += 1
        tournament_population.get_schedules().sort(key = lambda x: x.get_fitness(), reverse = True)
        return tournament_population
    
    def roulette_wheel_selection(self, population):
        population_fitness_sum = 0
        for schedule in population.get_schedules():
            population_fitness_sum += schedule.get_fitness()
        population_fitness_sum_half = population_fitness_sum / 2
        random_value = random.randrange(0, population_fitness_sum_half)
        spin_fitness_sum = 0
        for schedule in population.get_schedules():
            spin_fitness_sum += schedule.get_fitness()
            if spin_fitness_sum >= random_value:
                return schedule
        return population.get_schedules()[random.randrange(0, settings.POPULATION_SIZE)]

    def mutate_population(self, population):
        for i in range(settings.ELITISM_COUNT, settings.POPULATION_SIZE):
            self.mutate_schedule(population.get_schedules()[i])
        return population
    
    def crossover_schedule(self, schedule_1, schedule_2):
        crossover_schedule = schedule_1
        for i in range(len(schedule_1.get_classes())):
            if settings.CROSSOVER_RATE > random.random():
                crossover_schedule.get_classes()[i] = schedule_2.get_classes()[i]
        return crossover_schedule
    
    def mutate_schedule(self, mutate_schedule):
        schedule = Schedule(self.data).initialize() 
        for i in range(len(mutate_schedule.get_classes())): 
            if settings.MUTATION_RATE > random.random(): 
                mutate_schedule.get_classes()[i] = schedule.get_classes()[i] 
                
        return schedule

