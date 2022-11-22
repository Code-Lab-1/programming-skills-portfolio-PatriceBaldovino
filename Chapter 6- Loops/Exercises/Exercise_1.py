## Exercise 1: Pizza Toppings

    #Write a loop that prompts the user to enter a series of pizza toppings until
    #they enter a 'quit' value. As they enter each topping, print a message saying
    #you’ll add that topping to their pizza.

#print

prompt = '''
 ____                   
/    \	  What topping would you like on your pizza?
  u  u|      _______    
    \ |  .-''#%&#&%#``-.   
   = /  ((%&#&#&%&VK&%&))  
    |    `-._#%&##&%_.-'   
 /\/\`--.   `-."".-'
 |  |    \   /`./          
 |\/|  \  `-'  /
 || |   \     /           

'''
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        print("\nThank for ordering at Papajohns! ")
        break