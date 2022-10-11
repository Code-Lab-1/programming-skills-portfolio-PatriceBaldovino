## Exercise 3: Print date and Time :ballot_box_with_check:

    #Write a Python program to display the current date and time.

#Print the time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))