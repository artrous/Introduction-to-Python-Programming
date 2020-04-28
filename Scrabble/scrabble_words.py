# Scrabble Words

# The dictionary letters have the letters of the Greek language as keys
# and corresponding values ​​the points given each letter in Srabble

letters = {'Α':1,'Β':8,'Γ':4,'Δ':4,'Ε':1,'Ζ':10,
           'Η':1,'Θ':10,'Ι':1,'Κ':2,'Λ':3,'Μ':3,
           'Ν':1,'Ξ':10,'Ο':1,'Π':2,'Ρ':2,'Σ':1,
           'Τ':1,'Υ':2,'Φ':8,'Χ':8,'Ψ':10,'Ω':3
           }

my_words = {}         # Build the empty dictionary my_words to save pairs Word:Points_Word

while True:
    word = input('Word (or q for Exit): ')      # Read the input given by the player...

    if word == 'q':                             # ...and check for 'q' count
        break

    points = 0
    for ch in word:                     # In this loop the repeater ch takes as values ​​one after the other the letters that make up the word given as input
        points += letters[ch]           # The sum of points is added to the points corresponding to the letter ch

    print('Word Points:',points)       # The points of the word appear

    my_words[word] = points             # Enter in the dictionary my_words the pair word:points

for key in sorted(my_words):            # Call sorted() method for key-based classification, i.e. the keywords
    print(key, my_words[key])           # Appearance of couples Key:Value, i.e. key:my_words[key]    



# COMMENTS

# Watch out for the simplicity of Python in the loop:

##    for ch in word:
##        points += letters[ch]

# Writing: for ch in word
# 'Scan' all the characters (letters) of the word 'word' in a loop without the need for another iteration indicator
# Then putting the key character ch in the dictionary letters we have the value, i.e. the points that this letter gives
# to calculate the sum of all points in the sum of points
