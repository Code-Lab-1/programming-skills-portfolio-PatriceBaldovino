## Exercise 3: Your Own List

'''
    Think of your favorite mode of transportation, 
    such as a motorcycle or a car, and make a list 
    that stores several examples.

        Use your list to print a series of statements about
        these items, such as “I would like toown a Honda motorcycle.”
'''

## List of Transportation
fav_transpo = ['car','motorcycle','bus','airplane','taxi']

# Print 
print("\nWhat is your favorite mode of transportation?\n")
print("\t\"I love driving my {0}, it makes me feel safe.\"\n".format(fav_transpo[0]))
print("\nIs there any form of transportation that scares you?\n")
print("\t\"I think {0}s can be terrifying because its something I cannot control.\"\n".format(fav_transpo[3]))
print("\nIf you didnt have a {0} which mode of transportation would you use?\n".format(fav_transpo[0]))
print("\t\"I would probably use the {0} or {1} to go places, its cheaper that way.\"\n".format(fav_transpo[2],fav_transpo[4]))