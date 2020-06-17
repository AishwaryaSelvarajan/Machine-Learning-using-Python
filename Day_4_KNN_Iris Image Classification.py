import pandas as pd 
import matplotlib.pyplot as plt 

# Reading the Iris.csv file
data = pd.read_csv('Iris.csv')
print(data.head())

# This Dataset has 4 columns Sepal Length, Sepal Width, Petal Legth, Petal Width. Based on these parameters the flowers will be classified to any one of the species
# To find the unique data from a column
types_of_species = data['Species'].unique()
print(types_of_species)

# Divide the data into x and y
x = data.iloc[:,1:5].values # All the rows of 4 columns has been provided as input
y = data.iloc[:,5].values # The species column is the one to be predicted

# Divide the data into training and testing samples
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.20)

# Scaling/ Normalization of input data - The need for scaling is, if my data is in th erange of 0-50, i can scale it to 0-1 range, so that my computation will be fast
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
xtrain = sc.fit_transform(xtrain)
xtest = sc.fit_transform(xtest)

# Build the model
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 5) # Here n_neighbors is the value of K
# Generally the value of K is taken as Square root of total samples taken for training divided by 2.
# Calculated in that way here K takes the approximate value of 5

# Train the model
model.fit (xtrain,ytrain)

# As the model has been created, now the testing samples are used to predict y.
y_predict = model.predict(xtest)
print(y_predict)

# Now print the actual test values of y to compare predicted output of y and test value of y
print(ytest)

# To find variation between the test values and the predicted values we have a method called confusion matrix
# Confusion matrix is only for classification problems. If we have 2 class the output will be 2*2 matrix, 3 class 3*3 and so on

from sklearn.metrics import confusion_matrix
con_mat = confusion_matrix(y_predict,ytest)
print(con_mat)

# How to predict the accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_predict,ytest)
print(accuracy)

#If i want to predict the species for the new data I have using my model
species = model.predict([[1.2,2.3,4.5,2.1]])
print(species)