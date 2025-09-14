import numpy as np

company , valuation , datetime, City = np.genfromtxt("Startups in 2021 end.csv" , delimiter= "," , unpack= True  , usecols= [ 1,2,3,5] , invalid_raise= False, dtype= None, skip_header= 1)
print(company)
print(valuation)
print(datetime)
print(City)
valuation = np.char.replace(valuation, "$", "")
valuation = np.char.replace(valuation, ",", "")
valuation = valuation[valuation != ""]   # empty remove
# Convert to float
valuation = valuation.astype(float)
print("Mean:" , np.mean(valuation))
print("Median:" , np.median(valuation))
print("std:" , np.std(valuation))
print("Max:" , np.max(valuation))
print("Min:" , np.min(valuation))
print("Percentile 75:" , np.percentile(valuation , 75))
print("Percentile 25:" , np.percentile( valuation, 25))
print("Percentile 3:" , np.percentile( valuation, 3))
#Mathematical operations
print("Square:" , np.square(valuation))
print("Sqrt:" , np.sqrt(valuation))
print("Absolute value:" , np.abs(valuation))
print("Power:" , np.power(valuation , valuation))


# Float me convert karo
valuation = valuation.astype(float)

print(valuation)
addition = datetime + valuation
print("Addition:" , addition)