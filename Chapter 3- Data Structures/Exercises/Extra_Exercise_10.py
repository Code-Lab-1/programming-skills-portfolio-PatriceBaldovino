#Remove all occurrences of a specific item from a list.

'''
Given a Python list, write a program to remove all occurrences of item 20.

Work with the given list:
    list1 = [5, 20, 15, 20, 25, 50, 20]
'''

list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

rev = remove_value(list1, 20)
print(rev)