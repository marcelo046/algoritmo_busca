%matplotlib inline
import random
import matplotlib.pyplot as plt
import time

# declarações
size = 500 # não pode ser maior que max_number, pois dá erro no random.sample
loops = 25
max_number = 1000
x = []
time_sequential = []
time_binary = []

# comandos iniciais
for i in range(1, size+1):
    x.append(i)

#  funções
def gen_random_list():
    return random.sample(range(1, max_number), size)

def gen_order_list():
    list = random.sample(range(1, max_number), size)    #creating a list in range 0 to 100
    list.sort()    # ordering
    return list

def get_random_number():
    return random.randint(1,101)

def sequential_search(number):
    for k in range(0,len(list_numbers_any),1):
        if(number == list_numbers_any[k]): return k
    return -1

def binary_search(number):
    less = 0
    high = len(list_numbers_order) - 1
    update = 0
    while(less <= high):
        update = (less + high) // 2
        if(number < list_numbers_order[update]):
            high =update
        elif(number > list_numbers_order[update]):
            less = update
        else:
            return update

def gen_graph(list, title='plot of points'):
    plt.cla()
    plt.clf()
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('points')
    plt.plot( x , list , 'ro')
    plt.show()

def average_vector(vet): # tira a média de um vetor
    add = 0
    for i in range(0, len(vet), 1):
        add += vet[i]
    return add


# main

list_numbers_any = gen_random_list()
list_numbers_order = gen_order_list()

print("vetor de números em ordem crescente")
print(list_numbers_order)
gen_graph(list_numbers_order)
print("vetor de números em ordem aleatória")
print(list_numbers_any)
gen_graph(list_numbers_any)

# faz as buscas sequenciais
for it in range(0,loops,1):
    search_number_any = random.choice(list_numbers_any)
    #print(search_number_any)
    start_s = time.time()
    sequential_search(search_number_any)
    finish_s = time.time()
    time_sequential.append(finish_s - start_s)

# faz as buscas binárias
for it in range(0,loops,1):
    search_number_order = random.choice(list_numbers_order)
    #print(search_number_order)
    start_s = time.time()
    binary_search( search_number_order)
    finish_s = time.time()
    time_binary.append(finish_s - start_s)


time_1 = average_vector(time_binary)
time_2 = average_vector(time_sequential)

print("foram realizadas %d buscas em cada vetor de %d posições\n" % (loops, size))
print("O tempo medio  da  busca  binario é: ", time_1*1000, " milissegundos")
print("O tempo medio da busca sequencial é: ",time_2*1000, " milissegundos\n")
print("Nesse caso, a busca binaria foi cerca de %.2f vezes mais rápido que a sequencial" % (time_2 / time_1))
