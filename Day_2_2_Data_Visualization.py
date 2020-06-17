################## Data Visualization ##############################

# Draw a line plot by providing x axis values and y axis values
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6]
y_values = [6,10,3,5,12,3]

# Providing a title to the graph & label for both axes
plt.figure(figsize=(6,4))
plt.title('Line Plot Graph',fontsize = 15)
plt.xlabel('Time',fontsize = 15)
plt.ylabel('Velocity', fontsize = 15)
plt.plot(x_values,y_values,label = 'Line Plot', color = 'Purple')
plt.legend(loc=2)
plt.grid()
plt.show()

# Bar Plot
x_values = [1,2,3,4,5,6]
y_values = [10,20,30,40,50,60]
plt.figure(figsize=(6,4))
plt.title('Bar Graph',fontsize = 15)
plt.xlabel('Time',fontsize = 15)
plt.ylabel('Velocity', fontsize = 15)
plt.bar(x_values,y_values,label = 'Bar Graph', color = 'Pink')
plt.legend(loc=2)
plt.show()

# Scatter Plot
x_values = [1,2,3,4,5,6]
y_values = [3,2,4,2,4,1]
plt.figure(figsize=(6,4))
plt.title('Scatter plot',fontsize = 15)
plt.xlabel('Time',fontsize = 15)
plt.ylabel('Velocity', fontsize = 15)
plt.scatter(x_values,y_values,label = 'Scatter Plot', color = 'blue',marker='*')  # By default the scatter plot will be circles, to change that provide maerker argument  
plt.legend(loc=2)
plt.show()

# Histogram - First generate the required data for histogram
import numpy as np 
np.random.seed(1)
data = np.random.randint(1,100,50)
print(data)
plt.hist(data,rwidth=0.9,bins=7)
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
slices = [20,40,60,80]
activities = ['Travelling','Swimming','Cooking','Reading']
colours = ['red','yellow','green','blue']
plt.pie(slices,labels=activities,colors=colours,autopct='%1.2f%%',explode=(0,0,0.2,0))
plt.show()

# To save any of the figure
plt.savefig('Interests.eps')

# Plot a trignometric function
t = np.arange(0.0,0.2,0.01)
v = 1+np.cos(2*np.pi*t)
plt.plot(v,t)
plt.grid()
plt.show()

# Sub  Plot - Plotting two graphs in a single page
t1 = np.arange(0.0,2.0,0.01)
v1 = 1+np.cos(2*np.pi*t1)
t2 = np.arange(0.0,5.0,0.01)
v2 = 1+np.cos(2*np.pi*t2)
# Subplotfunction parameters, first value 2 is no. of rows, 2nd value 1 is no.of columns, third value is the position of the graph, whether it should be first or second
plt.subplot(2,1,1)
plt.plot(v1,t1)
plt.subplot(2,1,2)
plt.plot(v2,t2)
plt.grid()
plt.show()

