import numpy as np

ab = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
bc= np.array([1, 2, 3], ndmin = 5)
cd = np.array([[1, 2, 3], [4, 5, 6]])
de = np.array([23, 42, 73, 54, 65])
speed = [23,98,56,90,24,45,53,87,98,60]
x = np.mean(speed)
print(bc)
print(de[0])
print(de[2] + de[1])
#Sequential indexing for 3d elements
print(ab[1, 0, 1])
print("This shows elements 2nd to 4th in d array:", de[1:4])
#this prints from the second to last element in array d
print(de[1:])
#this prints the last element from array c
print("last element from c 2nd dim is:", cd[1, -1])
#This prints the second number in the second row from array c
print("The second number in the second row is:", cd[1, 1])
#This prints the number of dimensions in the b array
print("Number of dimensions:", bc.ndim)
#This prints the module  version number for numpy
print("My numpy console module version is:", np.__version__)
#This prints the type of a
print(type(ab))
#Exemption slicing
print(de[::1])
#Get Shape
print("The shape of the array is:", ab.shape)
#Get new shape
print(ab.reshape(4,3))
#Get data type
print(ab.dtype)
#Get size
print(ab.itemsize)
#Get total size
print(ab.nbytes)


a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
print(a)
print(a.shape)
#Get a specific element [r,c]
print(a[1,5])
#Get a specific row
print(a[1, :])
#Get a specific column
print(a[: ,4])
#Getting a little more fancy [startindex:endindex:stepsize]
print(a[1, 1:4:2])
#Element Replacement
a[1,5] = 16
print(a)

#3D EXAMPLE
b = np.array([[[1,2,3,4],[5, 6, 7, 8]],[[9,10,11,12],[13,14,15,16]]])
print(b)
print(b[1,0,3])


#INITIALIZING DATA ARRAYS
#ALL 0s Matrix
c = np.zeros((2,2,4))
print(c)
#ALL 1s MATRIX
d = np.ones((3,1,3))
print(d)
#Any Other Number
e = np.full((2,2), 4, dtype='float32')
print(e)
#any other number (full_like)
f = np.full_like(ab, 6)
print(f)
#random decimal number
g = np.random.rand(4,2)
print(g)
#Random Integer Number
h = np.random.randint(3,9, size=(3,2))
print("The value of h is:", h)
#The Identity matrix
i = np.identity(4)
print(i)
#Tuple Replication
j = np.array([[1, 2, 3]])
rj = np.repeat(j, 3, axis=0)
print(rj)

#CLASSWORK
k = np.ones((5,5))
l = np.zeros((3,3))
l[1,1] = 9
k[1:4,1:4] = l
print(k)
#### Be Careful when copying arrays
l = k.copy()
print(l)
print(k.base)
print(l.base)

#for idx,x in np.ndenumerate(n):
#print(idx,x)

#array iteration with enumeration
#jointarray = np.concatenate((n, o), axis=1)

#Array Joining
n = np.array([3, 4, 5, 6, 3, 3, 7, 9])
o = np.array([11, 12, 13, 14])
#arrayjoin = np.vstack((n, o))
#arrr = np.dstack((n, o))
#arr = np.array_split(n, 3)
p = np.where(n == 3)
q = np.where(n%2 == 0)
r = np.where(n%2 == 1)
#print(arr)
#print(arrr)
#print(arrayjoin)
print(p)
print(q)
print(r)

s = np.random.randint(50,100, size=(5,5))
print(s)
t = np.random.uniform(1.5,1.9, size=(3,3))
from numpy import random
u = random.choice([12, 23, 34, 45, 56, 67, 78, 89, 90])
w = random.choice([3, 5, 7, 9], p=[0.2, 0.2, 0.3, 0.3], size=(3,3))
print(w)
