import random
import matplotlib.pyplot as plt

# declarações
size = 20
x = []

# comandos iniciais
for i in range(1, size+1):
    x.append(i)

#  funções
def gen_random_list():
    return random.sample(range(1, 101), size)

def gen_order_list():
    list = random.sample(range(1, 101), size)    #creating a list in range 0 to 100
    list.sort()    # ordering
    return list

def gen_graph(list, title='plot of points'):
    plt.cla()
    plt.clf()
    #plt.close()
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('points')
    plt.plot( x , list , 'ro')
    plt.show()


# programa principal main
list_numbers_any = gen_random_list()
list_numbers_order = gen_order_list()

print(list_numbers_order)
print(list_numbers_any)

search_number_order = random.choice(list_numbers_order)
print(search_number_order)
search_number_any = random.choice(list_numbers_any)
print(search_number_any)
gen_graph(list_numbers_order)
gen_graph(list_numbers_any)
