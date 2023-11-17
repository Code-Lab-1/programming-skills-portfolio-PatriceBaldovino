## Exercise 4: Stages of Life

'''
    Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

    •If the person is less than 2 years old, print a message that the person is a baby.

    •If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

    •If the person is at least 4 years old but less than 13, print a message that the person is a kid.

    •If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

    •If the person is at least 20 years old but less than 65, print a message that the person is an adult.

    •If the person is age 65 or older, print a message that the person is an elder.
'''

#Variable
age = 3

#if-elif-else statement
if age < 2:
    print('''

     You're a baby!     lllllll_______
                     _,_  llllllllllll\\
        ___         /   \  llllllllllll\\
           \       | @ @ |  llllllllllll\\
            \-----oOO---Ooo-------------/
             \lllllllllllllllllllllllll/
              \lllllllllllllllllllllll/
               \lllllllllllllllllllll/
                   //            \\
                  ||             ||
                   OO             OO
    ''')
elif age < 4:
    print('''

   ,=""=,
  c , _,{   You're a toddler!
  /\  @ )                 __
 /  ^~~^\          <=.,__/ '}=
(_/ ,, ,,)          \_ _>_/~
 ~\_(/-\)'-,_,_,_,-'(_)-(_)    

    ''')
elif age < 13:
    print('''
        _         _
       / )%.===.%( \\
       | // ,,, \\\\ |
       \/ \/o.o\/ \/    You're a kid!
       /\ (  _  ) /\\
       ^^ /`"""`\ ^^
         ( (_@_) )
         /'-.Y.-'\\
        /    |    \\
       /___________\\
          _|_|_|_
         (___|___)

         ''')
elif age < 20:
    print('''
                         .-""". 
                        ///.   |
  You're a teenager!     )- \__/
                         \_  /
                        .-)_;-.
                       /       \\
                      /_/|   |\_\\
                      \ \|___|/ /
                       )|\   /|\\
                        |     |
                        |_____|
                         | | |
                         |-|-|
                         \ | /
                         /-T-\\
                        (_/ \_)     
    ''')
elif age < 65:
    print('''
    

      /:""|       .@@@@@,
     |:`66|_      @@@@@@@@,
     C`    _)     aa`@@@@@@     You're an adult!
      \ ._|      (_   ?@@@@
       ) /        =' @@@@"
      /`\\\\         \(```
     || |Y|       //`\\
     || |.|      / | ||
     || |.|      \ | ||
     || |.|       \| ||
     :| |=:        |_|\\
     ||_|,|        |_| \\
     \)))||        (((  |
      |  ||        |____|
      |  ||        |____|
      >  ))         | ||
      | ||          | ||
      | ||          | ||
      |_||__        /~))
     (____))      /_/YY    
    
''')
else:
    print('''
                     .---.
                    (_---_)
                   (_/6 6\_)
                    (  v  )
You're an elder!     `\ /'
                  .-'': ;``-.
                 /   \,Y./   \\
                /     (:)___  \\
               :   .-'XXX`-.`\_;
                `.__.-XXX-.__.'\_
                 /  / XXX \  \   `\_
                /      XXX    \     `\\
               /        XXX    \     _`\___
              /                 \  (`--"""-')
             /                   \ (=-=-=-=-)
             `--...___   ___...--' (________)   
           ''')