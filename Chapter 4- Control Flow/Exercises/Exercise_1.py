## Exercise 1:  Alien Colors

'''
    Imagine an alien was just shot down in a game.
    Create a variable called alien_color and assign it a
    value of 'green', 'yellow', or 'red'.

    •Write an if statement to test whether the alien’s color 
     is green. If it is, print a message that the player just earned 5 points.

    •Write one version of this program that passes the if test and
     another that fails. (The version that fails will have no output.)
'''

#Print of "You just earned 5 points"
alien_color = 'green'

if alien_color == 'green':
    print('''
o
/\_/\o
( Oo)                                        \|/
(_=-)  .===O-  ~~You~just~earned~5~points!~~ -O-
/   \_/U'                                    /|\\
||  |_/
\\\\  |
{K ||
 | PP
 | ||
 (__\\\\
    
    ''')

#The version that fails to print
alien_color = 'red'

if alien_color == 'green':
    print('''
o
/\_/\o
( Oo)                                         \|/
(_=-)  .===O-  ~~This~is~the~failed~version~~ -O-
/   \_/U'                                     /|\\
||  |_/
\\\\  |
{K ||
 | PP
 | ||
 (__\\\\
    
    ''')
