# filter is used to apply function on list
data = [1,3,4,5,5,12,3,21,31,45,112,34,31,43,42]
key_func = lambda x: x%2 == 0
even_data = filter(key_func, data)
print(f"Even numbers from list is {list(even_data)}")
odd_data = filter(lambda x: x%2 == 1, data)
print(f"Odd numbers from list is {list(odd_data)}")
