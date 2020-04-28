# Names & Registration Number

di = {}                         # Build a blank dictionary di

while True:
    inp = input('ΑΜ, Name (separated by a party) / q for Output: ')

    if inp=='q':                # Check first for q and then call split below
        break

    am, onoma = inp.split(',')  # This way we avoid the problem created by the split if two data are not given at the input
    am = int(am)                # Convert to int. It could also float
    di[am] = onoma              # The simplest way to enter pairs of data in dictionary: command assignment of the format Dictionary[Key] = Value

for key in sorted(di):          # Sorted gives a sorted keyword form of the dictionary 
    print(key, di[key])         # Appearance of couples Key:Value -> key:di[key]
