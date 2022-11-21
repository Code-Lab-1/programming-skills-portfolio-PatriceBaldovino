#Write a programm that ask for a number to the user and clasifies it:


print('''
   ___ ___
 /| |/|\| |\\
/_| ´ |.` |_\\
  |   |.  |
  |   |.  |
  |___|.__|
  ''')

#Input number
num = int(input("Enter your size number: "))
if num <= 2:
   print ("\n SMALL")
elif num <= 10:
   print ("\n MEDIUM")
else:
   print ("\n LARGE")
