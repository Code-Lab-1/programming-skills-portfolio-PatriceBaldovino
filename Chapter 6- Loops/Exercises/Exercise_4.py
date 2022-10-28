## Exercise 4: Deli

'''
Make a list called sandwich_orders and fill it with the names 
of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, 
such as I made your tuna sandwich. As each sandwich is made, move it to the list 
of finished sandwiches. After all the sandwiches have been made, print a message 
listing each sandwich that was made.
'''

#List 
sandwich_orders = ['Soobway Club', 'Veggie Delite', 'B.L.T', 'Roast Beef','Steak & Cheese']
finished_sandwiches = []

#Print of Sandwich
print('''
,_____________________________________________,
                    _.---._
                _.-~       ~-._
            _.-~               ~-._
        _.-~                       ~---._
    _.-~                                 ~\\
 .-~                                    _.;
 :-._                               _.-~ ./
 `-._~-._                   _..__.-~ _.-~
  /  ~-._~-._              / .__..--~----._
 \_____(_;-._\.        _.-~_/       ~).. . \\
    /(_____  \`--...--~_.-~______..-+_______)
  .(_________/`--...--~/    _/           /\\
 /-._     \_     (___./_..-~__.....__..-~./
 `-._~-._   ~\--------~  .-~_..__.-~ _.-~
     ~-._~-._ ~---------'  / .__..--~
         ~-._\.        _.-~_/
             \`--...--~_.-~
              `--...--~
._____________________________________________.

\t  Hello welcome to Soobway!
''')


#Sandwich order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")