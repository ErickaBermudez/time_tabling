POPULATION_SIZE = 5 # The number of schedules in each generation
CROSSOVER_RATE = 0.8 # The probability of a crossover occurring
MUTATION_RATE = 0.2 # The probability of a mutation occurring
NUMBER_OF_GENERATIONS = 10 # How many generations to run the algorithm for
ELITISM_COUNT = 1 # How many of the best schedules to keep from one generation to the next
"""
Selection pressure, a probabilistic measure of a chromosome's likelihood of participation 
in the tournament based on the participant selection pool size, is easily adjusted by changing the tournament size. 
The reason is that if the tournament size is larger, weak individuals have a smaller chance to be selected, because, 
if a weak individual is selected to be in a tournament, there is a higher probability that a stronger 
individual is also in that tournament.
"""
TOURNAMENT_SELECTION_SIZE = 3 # The number of schedules participating in tournament selection