## Exercise 5: Change Guest List 

    #You just heard that one of your guests can’t make the
    #dinner, so you need to send out a new set of invitations.
    #You’ll have to think of someone else to invite.

        #•Start with your program from Exercise 3-4. Add a print() call at 
        #the end of your program stating the name of the guest who can’t make it.

        #•Modify your list, replacing the name of the guest who can’t make it
        #with the name of the new person you are inviting.

        #•Print a second set of invitation messages, one for each person
        #who is still in your list.

## List of Guest
guests = ['Grell Sutcliff','Ciel Phantomhive','Sebastian Michaelis','Madam Red']

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

## Ciel Phantomhive cant make it to the dinner, lets invite someone else
del(guests[1])
guests.insert(1, 'Mey-Rin')

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