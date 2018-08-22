import random
size = 20
list_numbers_any = random.sample(range(1, 101), size) 
list_numbers_order = random.sample(range(1, 101), size)    #creating a list in range 0 to 100 
list_numbers_order.sort()    # ordering
print(list_numbers_order)
print(list_numbers_any)

search_number_order = random.choice(list_numbers_order)
print(search_number_order)
search_number_any = random.choice(list_numbers_any)
print(search_number_any)
