## Exercise 3: Print date and Time 

    #Write a Python program to display the current date and time.

#Print the time
import datetime
now = datetime.datetime.now()
print()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print()