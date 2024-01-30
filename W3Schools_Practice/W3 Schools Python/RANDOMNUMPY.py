import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

#data arrays
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
#functions
random.shuffle(a)
random.permutation(b)
#sns.displot([4, 5, 6, 7, 8, 9], hist=False) #Without Histogram
#sns.displot([1, 2, 3, 4, 5, 6]) #With Histogram
#sns.distplot(random.normal(size=1000), hist=False)
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial') #Binomial expression
random.normal(size=(2,3))
#output
print(a)
print(random.permutation(b))
print(random.normal(loc=4, scale=2, size=(2,3)))

#plt.show()