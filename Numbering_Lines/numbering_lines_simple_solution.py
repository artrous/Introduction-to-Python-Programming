# Numbering lines in a text file

try:
    with open('cities.txt','r') as fin:         # Open cities.txt
        cities = fin.readlines()                # Read the data with readlines() so that I have them in the form of a list
        try:
            with open('out.txt', 'w') as fout:          # Open out.txt to its own try..except administrator
                for index,line in enumerate(cities):    # index the pointer 0,1,.. and line, each line in the list of cities
                    newline = str(index+1)+': '+line    # Shape the line as the exercise demands
                    fout.write(newline)                 # Write to out.txt
        except Exception as err:
            print('Management error of out.txt: ', err)  # If an error occurs in with of out.txt
except Exception as err:
    print('Management error of cities.txt: ', err)       # If an error occurs in with of cities.txt
