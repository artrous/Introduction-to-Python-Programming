# Distance between two points on Earth

import math as ma
R = 6372.8 # Radius of earth in kilometers. Use 3956 for miles

lon1 = float(input('Give the Longitude1: '))
lat1 = float(input('Give the Latitude1: '))
lon2 = float(input('Give the Longitude2: '))
lat2 = float(input('Give the Latitude2: '))

# Haversine formula
# Convert decimal degrees to radians
dlon = ma.radians(lon2 - lon1)
dlat = ma.radians(lat2 - lat1)

a = ma.sin(dlat/2)**2 + ma.cos(ma.radians(lat1))*ma.cos(ma.radians(lat2))*ma.sin(dlon/2)**2
c = 2*ma.asin(ma.sqrt(a))

d = R*c
print('The distance between two points on the EARTH is: {:6.5f} km'.format(d))
