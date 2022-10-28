##Exercise 3: T-Shirt

'''
Write a function called make_shirt() that accepts a size and the text of a message that 
should be printed on the shirt. The function should print a sentence summarizing the size 
of the shirt and the message printed on it. 

Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.
'''
#Printer
print('''
  █▀ █░█ █ █▀█ ▀█▀   █▀█ █▀█ █ █▄░█ ▀█▀ █▀▀ █▀█
  ▄█ █▀█ █ █▀▄ ░█░   █▀▀ █▀▄ █ █░▀█ ░█░ ██▄ █▀▄
,______________________________________________,
  ,----,------------------------------,------.
  | ## |                              |    - |
  | ## |                              |    - |
  |    |------------------------------|    - |
  |    ||............................||      |
  |    ||,-                        -.||      |
  |    ||___                      ___||    ##|
  |    ||---`--------------------'---||      |
  `----'|_|______________________==__|`------'  
,______________________________________________,''')

#Function
def make_shirt(size, message):
    print("\nI will be using a " + size + " t-shirt.")
    print('It will say, "' + message + '"\n')

make_shirt('Extra large', 'I didn\'t sign up for this =|')
make_shirt(message = "ITS SHOWTIME!", size = 'small')