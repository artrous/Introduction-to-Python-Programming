# Image file check
# A solution that uses the sixteen-digit form of the byte value is the following:

jpgsign = 'ffd8ff'                  # Specify the signature of the jpg type as alphanumeric 'ffd8ff'

with open('imag', 'rb') as bf:       
    data = bf.read()                # Read the contents (i.e. the bytes values) of the imag file
    fsign = ''
    for i in data[:3]:              # Check the first three bytes
        ihex = hex(i)               # Create the hexadecimal form
        print(i,ihex)               # Display the required values ​​(in decimal and hexadecimal system)
        fsign = fsign+ihex[2:]      # Create the 'signature' fsign of the imag file as follows:
                                    # Because the sixteen-digit value is represented as alphanumeric eg. '0xff'...
                                    # Get the last two characters ihex[2:] and join for the first three bytes
                                    # If the imag file is indeed jpg the fsign will gradually get the 'ffd8ff' value
    
if fsign == jpgsign:                # Check if the fsign signature is the same as the jpgsign signature
    print('The file is type jpg')
else:
    print('The file is NOT a type jpg')
