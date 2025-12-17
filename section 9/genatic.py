import random
#  trying to solve N-Queens using genetic algorithm
# make population size from 0 to boardsize-1
def init_population():
    return [random.sample(range(board_size), board_size) for _ in range(population_size)]
# دالة عجلة الحظ 
# الهدف منه هو ان نصل لافضل حل بحيث نصل ال max_fitness or max_generation

def wheel_selection(population):
    fitness_scores = [p[1] for p in population]
    total_fitness = sum(fitness_scores)
    relative_fitness = [f / total_fitness for f in fitness_scores]
    cumulative_probability = [sum(relative_fitness[:i+1]) for i in range(len(relative_fitness))]
    rand = random.random()
    for i, cp in enumerate(cumulative_probability):
        if rand <= cp:
            return population[i]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, board_size - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child
# mutation by swap between  two position  => الطفره
def mutate(individual):
    pos1, pos2 = random.sample(range(board_size), 2)
    individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
    return individual
# count the number of pairs(i,j) queens that don't attack each other.
#This gives a larger score as the total number of attacks decreases.
def calc_fitness(individual):
    non_attacking = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

def solve_problem():
    global population
    global generation
    global best_fitness
# مرحلة التهيئه لكل فرد
    population = [(x, 0) for x in init_population()]
# calculate fitness foe every individual
    for generation in range(max_generation):
        population = [(individual, calc_fitness(individual)) for individual, _ in population]
# find best individual , best fitness
        best_individual = max(population, key=lambda x: x[1])[0]
        best_fitness = calc_fitness(best_individual)

# find the generation and stop if max_fitness == best_fitness
        if best_fitness == max_fitness:
            print("Solution found in generation", generation)
            break

        new_population = [max(population, key=lambda x: x[1])]
# choose 2 parents => يتم حسب نوع اختيار البطولة
        while len(new_population) < population_size:
            match tournament_selection_type:
                case 'roulette':
                    parent1 = wheel_selection(population)
                    parent2 = wheel_selection(population)
                case 'tournament':
                    # Stop if not defined
                    parent1 = wheel_selection(population)
                    parent2 = wheel_selection(population)
# انشاء طفل جديد
            child = crossover(parent1[0], parent2[0])
            if random.random() <= mutation_rate:
                child = mutate(child)
            new_population.append((child, 0)) # add child to new_population

        population = new_population
# print best solution 
    print("Best solution:", best_individual, "- Fitness", best_fitness, "- Generation:", generation + 1)

# Problem configuration
board_size = 8
max_fitness = int((board_size - 1) * board_size / 2)
population_size = 30
mutation_rate = 0.1
max_generation = 100
tournament_selection_type = 'roulette'
tournament_size = 3
tutorial_view = True

solve_problem()

