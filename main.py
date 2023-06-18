from data import Data
from classScheduling import Display, Population
import settings
from GA import GeneticAlgorithm

def main():
    print("==> Loading data")
    data = Data()
    print("==> Data loaded properly")
    print("# Number of classes: ", data.get_number_of_classes())

    display = Display()
    #print("=> Information about data")
    #display.print_data(data)

    print("==> Starting genetic algorithm")
    generation_number = 0
    population = Population(settings.POPULATION_SIZE, data)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    print("==> Initial population")
    display.print_generation(population)
    display.print_schedule(population.get_schedules()[0], generation_number)
    
    GA = GeneticAlgorithm(data)

    while population.get_schedules()[0].get_fitness() != 1.0:
        #print("==> Generation: ", generation_number)
        generation_number += 1
        population = GA.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        #print("Fitness: ", population.get_schedules()[0].get_fitness())
        
    print("==> Genetic algorithm finished")
    print("==> Final population")
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    display.print_generation(population)
    display.print_schedule(population.get_schedules()[0], generation_number)

if __name__ == "__main__":
    main()