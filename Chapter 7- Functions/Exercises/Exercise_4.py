#Exercise 4: Large Shirts

'''
    Modify the make_shirt() function so that shirts are large by default with a 
    message that reads I love Python. Make a large shirt and a medium shirt with 
    the default message, and a shirt of any size with a different message.
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

#Fuction
def make_shirt(size = 'large', message = 'I love Python'):
    print("\nI will be using a " + size + " t-shirt.")
    print('It will say,"' + message + '"\n')

make_shirt()
make_shirt(size = 'medium')
make_shirt('Extra Large','I didn\'t sign up for this =|')