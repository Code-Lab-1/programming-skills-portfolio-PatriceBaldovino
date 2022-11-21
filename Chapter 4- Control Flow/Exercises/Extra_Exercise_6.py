#Create a grading system. Using if-elif statement, create the following

'''
    - User is able to input their marks 
    - If the user inputs a score higher than 80 or equal to 90, then print A+
    - If the user inputs a score higher than 70 or equal to 80, then print A
    - If the user inputs a score higher than 60 or equal to 70, then print B
    - If the user inputs a score higher than 50 or equal to 60, then print C
    - If the user inputs a score higher than 40 or equal to 50, then print D
    - If the user inputs a score lower or equal to 30, then print "Failed"
    - If they dont input the score properly, then print "Something went wrong with the system"
'''
print('''
                     _____________________________________________
                    |  _________________________________________  |
                    | |                                         | |
                    | |                                         | |
                    | |                                         | |
               .-------------------------------------.          | |
              |  Here's your final scores, Once you   |         | |
              |         got it enter it here:         |         | |
               '-,-----------------------------------'          | |
       ___     _/   | |                                         | |
     .� __)         | |_________________________________________| |
    ( /_ _(\        |_____________________________________________|
   ( _|  > ))
  ( ( (---'-.
  (_ `)\-``  )
    `/-/   ) \\
----(__.�--------------.
\                       \\
\\\\_______________________\\
|,------------------------' 

''')
print('------------------------')
marks = int(input(" Enter your marks: "))
if marks>=80 and marks<=90:
  print(''' 
 ________________
|                |
|  A+ good job!  | 
|________________|\n''')
elif marks>=70 and marks<=80:
  print(''' 
 ________________
|                |
|  A nice job!   | 
|________________|\n''')
elif marks>=60 and marks<=70:
  print(''' 
 ________________________
|                        |
|  B  you can do better  | 
|________________________|\n''')
elif marks>=50 and marks<=60:
  print(''' 
 ________________
|                |
|  C study more  | 
|________________|\n''')
elif marks>=40 and marks<=50:
  print(''' 
 ________________
|                |
|  D study more  | 
|________________|\n''')
elif marks<=30:
  print(''' 
 ________________
|                |
|     Failed     | 
|________________|\n''')
else:
  print("\n Something went wrong with the system")
  