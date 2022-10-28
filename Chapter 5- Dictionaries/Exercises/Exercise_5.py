## Exercise 5: Pets

'''
    Make several dictionaries, where each dictionary represents a different pet. In each dictionary, 
    include the kind of animal and the owner’s name. Store these dictionaries in a list called pets.
    Next, loop through your list and as you do, print everything you know about each pet.
'''

#list to store the pets in.
pets = []

#Individual pets and store each one in the list.
pet = {
    'animal type': 'panda',
    'name': 'po',
    'owner': 'princess',
    'weight': 70,
    'eats': 'bamboo',
}
pets.append(pet)

pet = {
    'animal type': 'gorilla',
    'name': 'harambe',
    'owner': 'gladys',
    'weight': 200,
    'eats': 'celery',
}
pets.append(pet)

pet = {
    'animal type': 'deer',
    'name': 'bambi',
    'owner': 'frank',
    'weight': 60,
    'eats': 'grass',
}
pets.append(pet)

pet = {
    'animal type': 'shark',
    'name': 'bruce',
    'owner': 'robert',
    'weight': 547,
    'eats': 'humans',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))