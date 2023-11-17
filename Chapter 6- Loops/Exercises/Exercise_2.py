## Exercise 2: Movie Tickets

'''
    A movie theater charges different ticket prices depending on a person’s age. If a 
    person is under the age of 3, the ticket is free; if they are between 3 and 12, the
    ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which 
    you ask users their age, and then tell them the cost of their movie ticket.
'''

age_of_person = "\nHow old are you?"
age_of_person += "\nEnter 'quit' when you are finished. "

print('''
                @-_________________-@
          @-_____|   NOW SHOWING   |_____-@
           |    Spaceship   Soldiers     |
    _______|_____________________________|__________
   |________________________________________________|
   |               -                -               |
   |   -       -             -                    - |
   |        ____    ______________-   ____          |
   | -  -  |    |   |  TICKETS   |   |    | -       |
   |       |    |   |            |   |    |         |
   |  --   |____| - |_o___oo___o_| - |____|     -   |
   | -     |    |  |     --       |  |    |         |
   |    -  |    |- | -      -     |  |    | --      |
   |_______|====|__|______________|__|====|_________|
   /                                                 \\
  /___________________________________________________\\
''')

while True:
    age = input(age_of_person)
    if age == 'quit':
        print('''
          ____ _
         /////|\\\\
         ``````\\\\\\
         `/`    )))    Enjoy your movie!
         \`,   (((
          `--- ,\\\\\\
        ,---/ )),)))
       /  , `((  (((
       `--.   ) `__))       ________
       | |   ,-./\ \    _,-'
        \ \__,-.  \ \,-'
        /`.__,-'_,-\ `-.
       /       \____`--'____________
      |         \            
        ''')
        break
    age = int(age)

    if age < 3:
        print('''
        ╭――――――――――――――――――――――╮
        │                      │
        │   You get in free!   │
        │                      │
        ╰――――――――――――――――――――――╯
        ''')
    elif age < 13:
        print('''
        ╭―――――――――――――――――――――――╮
        │                       │
        │  Your ticket is $10!  │
        │                       │
        ╰―――――――――――――――――――――――╯
        ''')
    else:
        print('''
        ╭―――――――――――――――――――――――╮
        │                       │
        │  Your ticket is $15!  │
        │                       │
        ╰―――――――――――――――――――――――╯
        ''')