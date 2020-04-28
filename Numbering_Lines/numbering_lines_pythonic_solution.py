# A more Pythonic solution:

try:
    with open('cities.txt','r') as fin, open('out.txt', 'w') as fout:       # We can open the two files with this pension
        for index,line in enumerate(fin):               # The fin file object is already iterable so it can be used in for
            fout.write(str(index+1)+': '+line)          # We immediately write the new line form on fout
except Exception as err:                                
    print('Management error: ', err)          # If an error occurs, err will give us information
