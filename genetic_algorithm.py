from random import randint

import time
from object_individual import Individual

NUMBER_OF_ENTRIES = 16 # serao sorteados numeros de 0 ate 15 gerando 4bits

NUMBER_EXPECTED = 185
#MAX_VALUE = -1  # maximun value
MAX_RUNS = 100  # number maximun of executin
CUT_NUMBER = 4  # numero de corte para gerar nova populacao


def convert_integer_to_binary(integer):
    return bin(integer)[2:].rjust(4, '0')


def function(term_x, term_y, term_w, term_z):
    result_term_x = 5 * int(term_x)
    result_term_y = int(term_y) * int(term_y)
    result_term_w = int(term_w)
    result_term_z = int(term_z) * int(term_z) * int(term_z)
    return result_term_x + result_term_y + result_term_w + result_term_z


#definie os individuos aleatoriamente gerando os seus respectivos cromossomos
def __step_one():
    print('\n passo 1')
    step_one = []
    for var in range(10):
        term_x = randint(0, NUMBER_OF_ENTRIES - 1)
        term_y = randint(0, NUMBER_OF_ENTRIES - 1)
        term_w = randint(0, NUMBER_OF_ENTRIES - 1)
        term_z = -1
        #regra o z não pode ser maior que 5
        while term_z < 0 or term_z > 5:
            term_z = randint(0, NUMBER_OF_ENTRIES - 1)
        chromosome = convert_integer_to_binary(term_x) + convert_integer_to_binary(term_y) + convert_integer_to_binary(term_w) + convert_integer_to_binary(term_z)
        individual = Individual(term_x, term_y, term_w, term_z, chromosome)
        step_one.append(individual)

    print('Decimal | Binario')
    for obj in step_one:
        print(obj.print_not_weighting())
    return step_one


#aplica a fucao fitness
def __step_two(object_of_table):
    print('\n passo 2')
    for obj_step_two in object_of_table:
        obj_step_two.set_fun(function(obj_step_two.get_term_x(),obj_step_two.get_term_y(),obj_step_two.get_term_w(),obj_step_two.get_term_z()))

    for obj in object_of_table:
        print(obj.print_yes_weighting())


#aplica a ponderação 
def __step_three(object_of_table):
    print('\n passo 3')
    step_three = sorted(object_of_table, key=Individual.get_fun, reverse=True)
    for obj in step_three:
        print(obj.print_yes_weighting())
    return step_three


#estabelelce o corte dos individuos buscando pela proximidade com o valor esperado
def __step_four(object_of_table):
    i=0
    step_four = []
    while i < 6:
        if object_of_table[i].get_fun() <= NUMBER_EXPECTED:
            break
        i = i + 1
    j=4
    while j > 0:
        print('i',i)
        print('j',j)
        object_of_table[i].set_weighting(j)
        step_four.append(object_of_table[i])
        j = j -1
        i = i +1

    print('\n passo 4')
    for obj in step_four:
        print(obj.print_yes_weighting())
    return step_four

def sort_number_of_chromosomes():
    amount = 2#randint(1, 5)
    print('quantidade de cromossomos que seram utilizados para mutação: ', amount)
    direction = randint(0, 1)
    if direction == 1:
        print('começando a mutação de tras para a frente')
    else:
        print('começando a mutação da frente para tras')
    return amount, direction

def chromosome_convert(chromosome):
    returned = ''
    for chr in chromosome:
        #time.sleep(1.5)
        # num = randint(0, 100)
        # if num % 2 == 0:
        #     returned = returned + '0'
        # else:
        #     returned = returned + '1'
        returned = returned + str(randint(0, 1))
        #print(chr)
        # if chr =='0':
        #     returned = returned + '1'
        # else:
        #     returned = returned + '0'
    return returned


def replicate_population(individual,  amount, direction):
    replicate_population =[]
    replicate_population.append(individual) # salvando o pai na nova lista
    chromosome = str(individual.get_chromosome())
    chromosome_changed = ''
    chromosome_unchanged = chromosome
    new_chromosome = chromosome
    if direction == 0:
        chromosome_changed = chromosome[0:amount]
        chromosome_unchanged = chromosome[amount:len(chromosome)]
        new_chromosome = chromosome_convert(chromosome_changed) + chromosome_unchanged 
    else: #if direction == 1:
        chromosome_changed = chromosome[(len(chromosome) - amount):len(chromosome)]
        chromosome_unchanged = chromosome[0:(len(chromosome) - amount)]
        new_chromosome = chromosome_unchanged + chromosome_convert(chromosome_changed)

    #print('chromosome_changed', chromosome_changed)
    #print('chromosome_unchanged', chromosome_unchanged)
    #print('new_chromosome', new_chromosome)
   
    iteration = 0
    while iteration < individual.get_weighting() - 1:
        if direction == 0:
            new_chromosome = chromosome_convert(chromosome_changed) + chromosome_unchanged 
        else:
            new_chromosome = chromosome_unchanged + chromosome_convert(chromosome_changed)
        #for pop in amount_individual:
        replicate_population.append(Individual(chromosome=new_chromosome))
        iteration+=1
    ##print('test')
    #print(replicate_population.print_yes_weighting())
    return replicate_population


def create_new_population(object_with_weighting, amount, direction):
    children = []
    for individual in object_with_weighting:
        children = children + replicate_population(individual, amount, direction)
    return children

def __step_seven(step_four):
    amount, direction = sort_number_of_chromosomes()
    new_population = create_new_population(step_four, amount, direction) 
   
    print('\n passo 7')
    print('X | Y | Cromossomo | f(x,y) | Ponderação')
    for ff in new_population:
        print(ff.print_yes_weighting())
    
    return new_population

def __step_nine(step_seven):

    individual_position = []
    while True:

        num = str(randint(0, 9))
        if num not in individual_position:
            individual_position.append(num)
            if len(individual_position) == 5:
                break

    # for ff in individual_position:
    #     print(ff)

    for position in individual_position:
        individual = step_seven[int(position)]
        chromosome = individual.get_chromosome()
        num = randint(0, 5)
        #print('chromosome', int(position) + 1 , 'gene',num +1)
        #print('num',num)
        chromosome_changed_pre = chromosome[0:num]
        chromosome_changed_pos = chromosome[num + 1:len(chromosome)]
        chromosome_unchanged = chromosome[num]
        if chromosome_unchanged == '1':
            chromosome_unchanged = '0'
        else:
            chromosome_unchanged = '1'
        #print('chromosome_changed_pre', chromosome_changed_pre , 'chromosome_unchanged',chromosome_unchanged, 'chromosome_changed_pos',chromosome_changed_pos)
       
        individual.set_chromosome(chromosome_changed_pre + chromosome_unchanged + chromosome_changed_pos)

    print('\n passo 9')
    print('X | Y | Cromossomo | f(x,y) | Ponderação')
    for ff in step_seven:
        print(ff.print_yes_weighting())

def __step_ten(step_seven):
    for individual in step_seven:
        individual.convert_chromosome()

    print('\n passo 10')
    print('X | Y | Cromossomo | f(x,y) | Ponderação')
    for ff in step_seven:
        print(ff.print_yes_weighting())

def __step_eleven(step_seven):
    for individual in step_seven:
        individual.set_fun(function(individual.get_term_x(),individual.get_term_y(),individual.get_term_w(),individual.get_term_z()))
    
    step_eleven = sorted(step_seven, key=Individual.get_fun, reverse=True)
    for ff in step_eleven:
        ff.set_weighting(0)

    print('\n passo 11')
    print('X | Y | Cromossomo | f(x,y)')
    for ff in step_eleven:
        print(ff.print_not_weighting())
    return step_eleven


population = __step_one()
__step_two(population)
step_three = __step_three(population)

account_runs = 0
function_value = 0
step_eleven = step_three

while account_runs < MAX_RUNS:
    account_runs = account_runs + 1
    step_four = __step_four(step_eleven)
    new_population = __step_seven(step_four)
    __step_nine(new_population)
    __step_ten(new_population)
    step_eleven = __step_eleven(new_population)
    
    function_value = step_eleven[0].get_fun()
    if function_value == NUMBER_EXPECTED:
        break
print('finalizado com ', account_runs, ' épocas e valor da função encontrado ', function_value)


# # stepTwo
# __step_two()
# # stepThree
# step_three = __step_three()
#  # stepFour
# step_four = __step_four(step_three)

# account_runs = 0
# function_value = 0

# while account_runs < MAX_RUNS:
#     account_runs = account_runs + 1
   
#     # stepFive
#     step_five = __step_five(step_four)
#     # stepSix
#     step_six = __step_six(step_five)
#     # stepSeven
#     step_seven = __step_seven(step_six)
#     # step_nine
#     __step_nine(step_seven, account_runs)
#     # step_ten
#     step_ten = __step_ten(step_seven)
#     # step_eleven
#     step_eleven = __step_eleven(step_seven)

#     function_value = step_eleven[0].get_fun()
#     if function_value == NUMBER_EXPECTED:
#         break

# print('finalizado com ', account_runs, ' épocas e valor da função encontrado ', function_value)




# for obj in new_population:
#     obj.set_fun(function(obj.get_term_x(),obj.get_term_y(),obj.get_term_w(),obj.get_term_z()))

# print('-----------')
# for obj in new_population:
#     print(obj.print_yes_weighting())



# def __step_nine(step_seven, account_runs):

#     #if not (account_runs - 1) % 5 == 0:
#     #    return

#     individual_position = []
#     while True:

#         num = str(randint(0, 9))
#         if num not in individual_position:
#             individual_position.append(num)
#             if len(individual_position) == 5:
#                 break

#     # for ff in individual_position:
#     #     print(ff)

#     for position in individual_position:
#         individual = step_seven[int(position)]
#         chromosome = individual.get_chromosome()
#         num = randint(0, 5)
#         #print('chromosome', int(position) + 1 , 'gene',num +1)
#         #print('num',num)
#         chromosome_changed_pre = chromosome[0:num]
#         chromosome_changed_pos = chromosome[num + 1:len(chromosome)]
#         chromosome_unchanged = chromosome[num]
#         if chromosome_unchanged == '1':
#             chromosome_unchanged = '0'
#         else:
#             chromosome_unchanged = '1'
#         #print('chromosome_changed_pre', chromosome_changed_pre , 'chromosome_unchanged',chromosome_unchanged, 'chromosome_changed_pos',chromosome_changed_pos)
        
#         individual.set_chromosome(chromosome_changed_pre + chromosome_unchanged + chromosome_changed_pos)

#     print('\n passo 9')
#     print('X | Y | Cromossomo | f(x,y) | Ponderação')
#     for ff in step_seven:
#         print(ff.print_yes_weighting())


# def __step_ten(step_seven):
#     for individual in step_seven:
#         individual.convert_chromosome()

#     print('\n passo 10')
#     print('X | Y | Cromossomo | f(x,y) | Ponderação')
#     for ff in step_seven:
#         print(ff.print_yes_weighting())

# def __step_eleven(step_seven):
#     for individual in step_seven:
#         individual.set_fun(function(individual.get_point_x(), individual.get_point_y()))
    
#     step_eleven = sorted(step_seven, key=objects.get_fun, reverse=True)
#     for ff in step_eleven:
#         ff.set_weighting(0)

#     print('\n passo 11')
#     print('X | Y | Cromossomo | f(x,y)')
#     for ff in step_eleven:
#         print(ff.print_not_weighting())
#     return step_eleven

# # stepTwo
# __step_two()
# # stepThree
# step_three = __step_three()
#  # stepFour
# step_four = __step_four(step_three)

# account_runs = 0
# function_value = 0

# while account_runs < MAX_RUNS:
#     account_runs = account_runs + 1
   
#     # stepFive
#     step_five = __step_five(step_four)
#     # stepSix
#     step_six = __step_six(step_five)
#     # stepSeven
#     step_seven = __step_seven(step_six)
#     # step_nine
#     __step_nine(step_seven, account_runs)
#     # step_ten
#     step_ten = __step_ten(step_seven)
#     # step_eleven
#     step_eleven = __step_eleven(step_seven)

#     function_value = step_eleven[0].get_fun()
#     if function_value == NUMBER_EXPECTED:
#         break

# print('finalizado com ', account_runs, ' épocas e valor da função encontrado ', function_value)

