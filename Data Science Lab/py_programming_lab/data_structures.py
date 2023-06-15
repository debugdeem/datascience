# Lists
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list[0]) #1
my_list[0] = 0
for item in my_list:
    print(item)

# Dictionary
my_dict = {'name': 'John', 'age':25}
my_dict['height'] = 160
print(my_dict['name'])
my_dict['name'] = 'Doe'
for key, value in my_dict.items():
    print(key, value)

# Set
my_set = {1, 2, 3}
print(my_set)
my_set.add(4)
print(my_set)

# Tuple
my_tuple = (1, 2, 3)
print(my_tuple[0])