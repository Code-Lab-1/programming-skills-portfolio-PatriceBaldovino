##Exercise 5: No Pastrami

'''
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich
'pastrami' appears in the list at least three times. Add code near the beginning
of your program to print a message saying the deli has run out of pastrami, and 
then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 

Make sure no pastrami sandwiches end up in finished_sandwiches.
'''

#List 
sandwich_orders = ['Pastrami','Soobway Club', 'Veggie Delite', 'B.L.T', 'Roast Beef','Steak & Cheese',
'Black Forest Ham', 'Buffalo Chicken']
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

print("I'm sorry to inform you that we're all out of pastrami :(")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")