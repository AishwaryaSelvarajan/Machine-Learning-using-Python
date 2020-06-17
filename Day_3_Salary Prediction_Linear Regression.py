import pandas as pd 
import matplotlib.pyplot as plt

# Read the data file which is Salary_Data.csv
data = pd.read_csv("Salary_Data.csv")

# Print the first five rows of Salary_Data.csv by using head() function
print(data.head())

# Lets take the Years of Experience column as x and Salary as y, this is because we have to find a function of x to get y
x = data.iloc[:,0].values # iloc is to save all the rows of 0 th column(Years of Experience) of data file to x
y = data.iloc[:,1].values # iloc is to save all the rows of 1 st column(Years of Experience) of data file to y

# or
# x = data.iloc[:]['YearsExperience'].values # iloc is to save all the rows of 0 th column(Years of Experience) of data file to x
# y = data.iloc[:]['Salary'].values # iloc is to save all the rows of 1 st column(Years of Experience) of data file to y

# Now the shape of the x and y array is 1D, but to plot in a 2 D space I need a 2Darray
print(x.shape)
print(y.shape)

# To convert x and y to 2D array
x = x.reshape(len(x),1)
y = y.reshape(len(y),1)

# Divide the data into Training and Testing Samples
from sklearn.model_selection import train_test_split # This module is to split the testing and training sample
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.20) # The test size is given as 0.20, means 80% of x and y will be training date, 20% of x and y will be testing data

# Buid the model (Linear Regression)
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Train the model
model.fit(xtrain,ytrain)

# As the model has been created, now the testing samples are used to predict y.
y_predict = model.predict(xtest)

# Printing the predicted Values and the test values of y
print(y_predict)
print(ytest)

# To check the accuracy whethermy predicted outputis almost near to the test data
from sklearn.metrics import r2_score
accuracy_r2 = r2_score(ytest,y_predict)
print('The accuracy is '+ str(accuracy_r2))

# To print the m and the y intercept c
m_slope = model.coef_
c_y_intercept = model.intercept_
#print('The slope is : ' + m_slope)
#print('The y intercept, c is: '+ c_y_intercept)

# How do i predict the Salary for 20.1 years of experience
Salary = model.predict([[20.1]])
print(Salary)

# Plotting the line of regression for Training Samples
plt.scatter(xtrain, ytrain, color = 'purple')
plt.plot(xtrain, model.predict(xtrain), color = 'red')
plt.show()

# Plotting the line of regression for Testing Samples
plt.scatter(xtest, ytest, color = 'purple')
plt.plot(xtest, model.predict(xtest), color = 'red')
plt.show()

# Once I am satisfied with the model I have to save it.
from sklearn.externals import joblib
joblib.dump(model,'mymodel.pkl')

# To load my model
mymodel = joblib.load('mymodel.pkl')

# Now once mymodel has been loaded i can predict the Salry by providing the years of experience
Salary_mymodel = mymodel.predict([[19.1]])
print(Salary_mymodel)


