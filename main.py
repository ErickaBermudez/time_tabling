from data import Data
from classScheduling import Display, Population
import settings

def main():
    print("=> Loading data")
    data = Data()
    print("=> Data loaded properly")
    print("# Number of classes: ", data.get_number_of_classes())

    display = Display()
    #print("=> Information about data")
    #display.print_data(data)

    print("=> Starting genetic algorithm")
    generation_number = 0
    population = Population(settings.POPULATION_SIZE, data)
    print("=> Generation: ", generation_number)
    display.print_generation(population)
    display.print_schedule(population.get_schedules()[0], 0)


if __name__ == "__main__":
    main()