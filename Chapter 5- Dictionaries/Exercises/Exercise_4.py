## Exercise 4: Rivers

    #Make a dictionary containing three major rivers and the country each river runs through. 
    #One key-value pair might be 'nile': 'egypt'.

    #* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

    #* Use a loop to print the name of each river included in the dictionary.

    #* Use a loop to print the name of each country included in the dictionary.

#Dictionary
rivers = {
    'Pasig River': 'Philippines',
    'Shinano River': 'Japan',
    'Ganges': 'India',
    'Po': 'Italy',
    'Loire': 'France',
    }

for river, country in rivers.items():
    print("\nThe " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())