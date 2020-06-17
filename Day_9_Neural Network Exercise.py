# Problem Statement
# I have 3 inputs x1,x2,x3 and output as y. We are going to give those inputs to the NN and get the output

import numpy as np
# 4 Samples of input has been provided
input_NN = np.array([[0,1,0],[0,0,1],[1,1,1],[1,0,1]])
print(input_NN)

# Relevant output
output_NN = np.array([[0],[0],[1],[1]])
print(output_NN)

# Providing weights
np.random.seed(10)
weights = np.random.random(3)
print("The weights are: ")
print(weights)

# Sum of the dot product of inputs and weights
sum_of_weights_and_input = np.dot(input_NN,weights) + 0.02 # 0.02 is the bias
print(sum_of_weights_and_input)

# Create the Activation function, sigmoid function
def sigmoid(x):
    return 1/ (1+np.exp(-x))

# Choosing gradient descent to minimise the error
def gradient(x):
    return x * (1-x)

for i in range (1500):
    # Sum of the dot product of inputs and weights
    sum_of_weights_and_input = np.dot(input_NN,weights) + 0.02 # 0.02 is the bias
    print(sum_of_weights_and_input)
    # Passing the sum to the sigmoid function
    pred_output = sigmoid(sum_of_weights_and_input)
    print("The predicted output is : ")
    print(pred_output)
    error = output_NN - pred_output
    print("The error is: ")
    print(error)
    # Applying the gradient Descent
    adjustment = error * gradient(pred_output)
    # Apply the Back - propogation
    weights += np.dot(input_NN.T,adjustment)
print(error)

print(pred_output.round())


