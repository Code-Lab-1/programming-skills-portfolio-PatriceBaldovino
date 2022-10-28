## Exercise 1: Person 

'''
    Use a dictionary to store information about a person you know. Store their first name, 
    last name, age, and the city in which they live. You should have keys such as first_name, 
    last_name, age, and city. Print each piece of information stored in your dictionary.
'''

#Dictionary
person = {
    'first_name': 'Johan',
    'last_name': 'Liebert ',
    'age': '23',
    'city': 'Prague\n',
    }

#Printing of output

print('''
               __                                         
             .'  `""*****------------........________     
            /      _______...........______________  `\   
           : .j"""'                  ___  __  _    `T`*;  
           |/ :     |   |  /\  |\  |  |  |   | \    |     
              `;    | ^ | :__: | \ |  |  |-  |  ;   |     
               |    |/ \| |  | |  \|  |  |__ |_/ .-*'     
               |      ____....ssssssss....____    `".     
               |    .P""""""""""""""""""""""""T.    |     
                `-. T      ,'         \        T    |     
               .-'  ;     :   ,*'"*v*"*;       :    |     
               |    |     |  /         |       |    |     
               |    |     ,-: .*"    "*;       |    |     
               |    |     ;P     |       |    :     
               ;    |     `-.      ,   |       |  .'      
               ;    |       :   '.___. '       |  `.      
               :    |       |`.    -  /        |    ;     
               `;   |     _.:  `-.__.'         |    |     
                `-, ; ,-*'   `-.__.-''*-._     :    |     
               ,-': b:                    `.   d    |     
              :     `b________________________d'   /,     
              |       """"****T$$$$$$P****""""     "|     
              `;     _   __              _   _      |     
               `;   | \ |   |   |   /\  | \ | \     |     
              ._|   |_/ |-  | ^ |  :__: |_/ |  ;  ,',     
              `.    | \ |__ |/ \|  |  | | \ |_/    `|     
                ;        _     _     _     _    .|-,`,    
                |   /|  / \   / \   / \   / \  (_|_  :    
             __ :    | :   ; :   ; :   ; :   ;   | ) |    .
             \ `'-._ |  \_/   \_/   \_/   \_/  `-|"  |   /;
              \     `***-----...__     _____.....----+-*'/ 
               `-.__...-----...   `:,-'               _.'  
                               `**--..____...----***''     
 .__________________________________________________________________.''')

print("\n  Name: " + person['first_name'])
print("  Family Name: " + person['last_name'])
print("  Age: " + person['age'])
print("  City Last Seen: " + person['city'])