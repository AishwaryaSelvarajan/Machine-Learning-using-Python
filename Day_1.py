################################### NUMPY Basics ##############################

import numpy as np 

# Create a 1 - Dimensional Array using numpy
a1 = np.array([1,2,3,4,5,6])
print (type(a1))
print (a1)

# Create a 2 - Dimensional Array using numpy
a2 = np.array([[1,2,3,4],[5,6,7,8],[10,11,12,13]])
print (type(a2))
print (a2)

# How to get the shape of the array - how many number of rows and columns
#print("Number of rows and columns of 2-Dimensional array is " + a2.shape)
print(a2.shape)

# How to get the number of dimensions?
print("The number of dimension of the array " + str(a2.ndim))

# How to get the number of elements in the array
print("The number of elements in the array is " + str(a2.size))

# Create a 3 - Dimensional Array using numpy
a3 = np.array ([[[1,2,3,4],[5,6,7,8],[10,11,12,13]]])
print (a3)

# Printing the length of 2- Dimensional Array
print("Length of 2 - Dimensional Array " + str(len(a2)) + " because I have 3 elements/ 3 rows in the list")

# Printing the length of a 3 - Dimensional Array
print ("Length of 3 - Dimensional array is " + str(len(a3)) + " because in a 3D array one 2D array will be considered as a single element")

# Picking the element of the array - Picking from a2 - a2 has three elements with index 0,1,2 and 0th index has 4 elements and same with 1 st and 2nd index
print("The element in row 1 and column 1 of a2 array is " + str(a2[1][1])) # or
print ("The element in row 1 and column 1 of a2 array is " + str(a2[1,1]))

# To print a row of an array use the technique of slicing
print(a2[:])
print(a2[1:3])

# Printing the column elements from all rows
print (a2[:,1])
print(a2[:,1:4])

# Change the shape of the 2D array
a2.reshape(4,3)

# Finding the mean in 2D array
print("The mean of the a2 array is " + str(a2.mean()))

# Finding the maximum element in the array
print("The maximum element of the a2 array is " + str(a2.max()))

# Finding the minimum element in the array
print("The minimum element of the a2 array is " + str(a2.min()))

# Finding the position of the maximum and minimum element in an array
print("The position of the maximum element is " + str(a2.argmax()))
print("The position of the minimum element is " + str(a2.argmin()))

# Calculating the sum of elements row wise and column wise
print(a2.sum(axis=1))  # axis = 1 means sum of rows
print(a2.sum(axis=0))  # axis = 0 means sum of columns

# Creating a Zeros, Ones and Identity Matrix
zero_matrix = np.zeros((5,5))
print (zero_matrix)

one_matrix = np.ones((5,5))
print(one_matrix)

Identity_matrix = np.identity(5,dtype = int)
print(Identity_matrix)

# To find the datatype of the matrix elements of zero_matrx and one_matrix
print(zero_matrix.dtype)
print(one_matrix.dtype)

# By default the array elemets are floating point numbers. To convert the elements to int 
print(zero_matrix.astype('int'))
print(one_matrix.astype('int'))

# Generate some equidistance between a range -  say i want to generate a sample of 30 numbers from 1 - 100
equidistant_array = np.linspace(1,100,num=30, dtype=int) 
print(equidistant_array)

# If equidistant array has to be incremented stepwise
equidistant_array_step = np.arange(1,100,3)

# Generate some random numbers
random_number = np.random.randint(1,100)
print("A random number from 1 to 100 is " + str(random_number))

# If i want 10 random numbers from 10 to 100
array_of_random_numbers = np.random.randint(1,100,10)
print (array_of_random_numbers)

# If i want to have the same sample again and again
np.random.seed(1)
print(np.random.randint(1,100,10))

# If i wanted to print an matrix of random numbers
np.random.seed(1)
print(np.random.randint(1,100,(3,3)))


###################################### PANDAS Basics ###############################

# Creating a Series
import pandas as pd 
marks = [50,55,90,97,85,86] # This is an simple list of marks
marks_as_series = pd.Series(marks)
print(marks_as_series)

# In the previous series created index will be printed along with the list values. If index values has to be replaced with any other string, then the ollowing code is used
subject = ['Tamil','English','Maths','Science','History','Geography']  # This can be tuple also
marks_as_series = pd.Series(marks,index=subject)
print(marks_as_series)

# Series with Dictionaries
subject_marks = {'Tamil':90, 'English':91, 'Maths':84,'Science':78,'History':80,'Geography':97}
marks_as_dict = pd.Series(subject_marks)
print(marks_as_dict)

total_marks = marks_as_series + marks_as_dict
print(total_marks)

# To print the first 5 output in a series we can use head() function, to print the last 5 output in a series we can use tail() function
print(total_marks.head())
print(total_marks.tail())

# To print the data of any row - iloc
print(total_marks.iloc[3])

# To print the data of any row by providing the Key - loc
print(total_marks.loc['Maths'])

# Sorting of data
print(total_marks.sort_values) # By default it will be sorted in ascending order
print(total_marks.sort_values(ascending=False)) # Sorting will be in descending order







