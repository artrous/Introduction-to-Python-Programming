# Double-ended queue or Deque

dqueue = []                                 # I create the list (queue) which is empty at the beginning
inp = None

while True:
    inp = input('Entry can be: Datum / 0Datum / r / 0r / q : ')
    
    if inp == 'q':                          # I check for 'q' entry
        break
     
    if 'r' in inp:                          # I check if 'r' is included
        if inp[0]=='0':                     # If it precedes 0
            dqueue.pop(0)                   # I remove the first item from the queue with method pop(0)
        else:
            dqueue.pop()                    # Otherwise I remove the last item from the queue simply with pop()
    else:                                   # Otherwise: (If 'r' is NOT included)
        if inp[0]=='0':                     # I check the first item if it is 0
            dqueue.insert(0,inp[1:])        # I enter the data in position 0, at the beginning of the queue
        else:                  
            dqueue.append(inp)              # Otherwise I enter the data at the end of the queue
                                 
    print(dqueue)


# COMMENTS

# When I remove data I can write conditional expression to check and in case the queue is empty
# For example:

##if inp[0]=='0':
##    dqueue.pop(0) if len(dqueue)>0 else print(Empty queue!')

# In the solution I give, I treat the data as alphanumeric (str)
# If necessary I can call int() or float() and convert them to integer or real values
