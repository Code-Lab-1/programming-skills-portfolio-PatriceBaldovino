## Exercise 2: Alien Colors

    #Choose a color for an alien as you did in Exercise 5-3,
    #and write an if-else chain. 

    #•If the alien’s color is green, print a statement that
    #the player just earned 5 points for shooting the alien.

    #•If the alien’s color isn’t green, print a statement that the 
    #player just earned 10 points.

    #•Write one version of this program that runs the if
    #block and another that runs the else block.

#Print of the if part:
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
else:
    print('''

   You just earned 10 points! 
                             | .-.
                .-""`""-.    |(@ @)
             _/`oOoOoOoOo`\_ \ \-/
            '.-=-=-=-=-=-=-.' \/ \\
              `-=.=-.-=.=-'    \ /\\
                 ^  ^  ^       _H_ \\
    ''')

#Print of the else part:
alien_color = 'red'

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
else:
    print('''

   You just earned 10 points! 
                             | .-.
                .-""`""-.    |(@ @)
             _/`oOoOoOoOo`\_ \ \-/
            '.-=-=-=-=-=-=-.' \/ \\
              `-=.=-.-=.=-'    \ /\\
                 ^  ^  ^       _H_ \\
    ''')

