import numpy as np 

address,city,country,longitude,latitude= np.genfromtxt("fastfood/FastFoodRestaurants.csv",delimiter=",", usecols=(0,1,2,4,5), unpack= True , dtype= None , skip_header= 1,invalid_raise=False)
print(address) 
print(city)
print(country)
print(longitude)
print(latitude)