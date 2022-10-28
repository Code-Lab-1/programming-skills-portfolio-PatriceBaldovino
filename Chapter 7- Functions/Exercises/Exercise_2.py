##Exercise 2: Favorite Book

'''
Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as One of my favorite books is 
Alice in Wonderland. Call the function, making sure to include a book title 
as an argument in the function call.
'''
#Function
def favorite_book(title):
    print('''
    _    
   /.)   
  /)\| '''+ title + " is one of my favorite book")
    print(''' //)/
/'\"^\"\n''')

favorite_book("The Six of Crows")