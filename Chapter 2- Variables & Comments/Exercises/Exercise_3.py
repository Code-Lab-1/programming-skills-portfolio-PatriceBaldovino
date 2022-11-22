## Exercise 3: Stripping Names 

'''
    Tidy up the code to make it easier to understand
    Use a variable to represent a person’s name, and 
    include some whitespace characters at the beginning 
    and end of the name. Make sure you use each character
    combination, “\t” and “\n”, at least once.
'''

    #Print the name once, so the whitespace around the name is displayed. 

#Variable
name = "\tLoid Forger\n"

#Normal
print("Normal: ")
print(name)

#Using lstrip()
print("\nUsing lstrip():")
print(name.lstrip())

#Using rstrip()
print("\nUsing rstrip():")
print(name.rstrip())

#Using strip()
print("\nUsing strip():")
print(name.strip())