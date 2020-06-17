######################### PANDAS Basics continued from Day 1 ######################################

# Creating a Series
import pandas as pd
import openpyxl, xlrd
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

# To create a Data Frame
dataframe = pd.DataFrame(total_marks)
print(dataframe)

# The index column which is the subjects must be provided with Column names
dataframe = dataframe.reset_index()  # By default the column name will be index
print(dataframe)

# How to rename the two columns
dataframe = dataframe.rename(columns={'index':'Subjects', 0:'Marks'})
print(dataframe)
# or if the dataframe variable is not assigned the above line of code can be changed as dataframe.rename(columns={'index':'Subjects', 0:'Marks'}, inplace = True)

# Adding a column to the dataframe
dataframe['School Name'] = 'Vishnu Lakshmi' # This will add the same School name to all the rows

# Adding a column with different values
dataframe['Teacher Name'] = ['Rajesh','Vanitha','Geetha','JayaSudha','Rose','Merlin']
print(dataframe)

# To print any required columns
print(dataframe[['Subjects', 'Teacher Name']])

# If any of the value in a column is Nan, and if we have to fill any default value instead of Nan then use the following code
# dataframe['Marks'] = dataframe['Marks'].fillna(<default value>)

# If I have to add a new column called grades, with marks greater than 150, it should be A grade, if marks is less than 150 then grade is B
grade = []  # Empty list

for i in range(0,len(dataframe)):
    mark = dataframe.iloc[i]['Marks']
    if mark >= 150:
        grade.append('A')
    else:
        grade.append('B')

dataframe['Grade'] = grade
print(dataframe)

# Sort the data according to Marks
dataframe = dataframe.sort_values('Marks',ascending = False)
print(dataframe)

# Now the index will also be sorted. So I am going to reset the index
dataframe = dataframe.reset_index()
print(dataframe)

# How to drop a column
dataframe = dataframe.drop(['index'], axis=1)
print(dataframe)

# How to drop a row
dataframe = dataframe.drop([3],axis=0)
print(dataframe)

# To replace any value in the dataframe
dataframe = dataframe.replace(to_replace = 'Rajesh', value = 'Raja')
print(dataframe)

# Export the data to excel 
dataframe.to_excel('Maksheet.xlsx')

# To import the Excel again
data = pd.read_excel('Maksheet.xlsx')
data.head()
