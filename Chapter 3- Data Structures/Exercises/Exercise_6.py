## Exercise 6: Shrinking Guest List

'''
    You just found out that your new dinner table won’t arrive in time 
    for the dinner, and you have space for only two guests.

        •Start with your program from Exercise 3-5. Add a new line thatprints 
         a message saying that you can invite only two people for dinner.

        •Use pop() to remove guests from your list one at a time until only two 
         names remain in your list. Each time you pop a name from your list, print 
         a message to that person letting them know you’re sorry you can’t invite 
         them to dinner.

        •Print a message to each of the two people still on your list, letting
        them know they’re still invited.

        •Use del to remove the last two names from your list, so you have an 
        empty list. Print your list to make sure youactually have an empty 
        list at the end of your program.
'''

## List of Guest
guests = ['Grell Sutcliff','Ciel Phantomhive','Sebastian Michaelis','Madam Red']

    ## Invitation Print
# First guest
name = guests[0].title() #Same as the previous exercise code for invitation
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

# Second guest
name = guests[1].title()
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

# Third guest
name = guests[2].title()
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

# Fourth guest
name = guests[3].title()
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

## Ciel Phantomhive cant make it to the dinner, lets invite someone else
del(guests[1])
guests.insert(1, 'Elizabeth Midford')

print('''
---------------------------------------------------------------------
        .------------------------------------------------.
        | Dear The Royal Palace,                         |
        |                                                |
        |      It saddens me to inform you that the      |  
        |     Earl Ciel Phantomhive will not be able     | 
        |          to attend the festivities.            |
        |                                                |
        |                  - Sincerly Ciel Phantomhive   |
        \'------------------------------------------------\'
---------------------------------------------------------------------
''')

    ## Invitation Print
# First guest
name = guests[0].title()
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

# Second guest
name = guests[1].title()
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

# Third guest
name = guests[2].title()
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

# Fourth guest
name = guests[3].title()
print('''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

\"Greetings {0}, you are invited to the royal dinner."\n
            \"This dinner will be held in the Palace!\"

'''.format(name))

# Oh no, the table won't arrive on time!
print('''   
.---------------------------------------------------------------.
|                                                               |
|   Sorry to inform, we can only invite two people to dinner.   |
|                                                               |
'---------------------------------------------------------------'
''')

name = guests.pop()
print(f'''
            
           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

          Sorry, {name.title()} there's no room at the table.\n''')

name = guests.pop()
print(f''' 

           █▀█ █▀█ █▄█ ▄▀█ █░░  █▀▄ █ █▄░█ █▄░█ █▀▀ █▀█
           █▀▄ █▄█ ░█░ █▀█ █▄▄  █▄▀ █ █░▀█ █░▀█ ██▄ █▀▄

      Sorry, {name.title()} there's no room at the table.''')

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)
