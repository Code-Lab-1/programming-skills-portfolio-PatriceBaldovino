## Exercise 5: Favorite Fruit

'''
    Make a list of your favorite fruits, and then write a series of
    independent if statements that check for certain fruits in your list.

    •Make a list of your three favorite fruits and call it favorite_fruits.

    •Write five if statements. Each should check whether a certain kind of 
    fruit is in your list. If the fruit is in your list, the if block should 
    print a statement,such as You really like bananas! 
'''

##List of favorite fruits
favorite_fruits = ['kiwis', 'strawberries', 'oranges']

if 'bananas' in favorite_fruits:
    print('''
     ,                                 ,
     \`.__.  You really like bananas!  \`.__.
      `._,'                             `._,'
''')
if 'apples' in favorite_fruits:
    print('''
      ,(.                             ,(.
     (   )  You really like apples!  (   ) 
      `"'                             `"'
      ''')
if 'grapefruit' in favorite_fruits:
    print('''
      ,;:.                                 ,;:.
     (::;;)  You really like grapefruit!  (::;;)
      `;:'                                 `;:'
''')
if 'kiwis' in favorite_fruits:
    print('''
      _                            _
     (:)  You really like kiwis!  (:)
      "                            " 
''')
if 'oranges' in favorite_fruits:
    print('''
     ,=.                              ,=.
    (.`:)  You really like oranges!  (.`:)
     `-'                              `-'  
''')

