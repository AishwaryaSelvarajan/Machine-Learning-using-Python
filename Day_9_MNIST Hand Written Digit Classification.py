import tensorflow.keras as tf 
import numpy as np
import matplotlib.pyplot as plt
import cv2

mnist = tf.datasets.mnist
(xtrain,ytrain),(xtest,ytest) = mnist.load_data()

print("The shape of Training data: ")
print(xtrain.shape)

# There are 60000 samples for training. To display the 16th sample 
plt.imshow(xtrain[15],cmap = 'gray')
plt.show()

# Create the blank model of Neural Network
model = tf.models.Sequential()

# Add the layers. How many minimum layers should be added?
# Add the input layer
model.add(tf.layers.Flatten())

# Add the hidden layer
model.add(tf.layers.Dense(784,activation='relu')) # As the image shape is 28*28, we have given 784

# Add the Output layer
model.add(tf.layers.Dense(10,activation='softmax'))

# Scale/ Normalise the data
xtrain = xtrain/255
xtest = xtest/255

# compiling the model
model.compile(loss = 'sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

# Train the model
model.fit(xtrain,ytrain,batch_size=30,epochs=15)

# Test first 25 samples of training
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([]) # This is to ignore the co-ordinates
    plt.yticks([])
    plt.imshow(xtest[i],cmap='gray')
    plt.xlabel(np.argmax(ypred[i]),fontsize=15)
plt.show

model.evaluate(xtest,ytest)

# Test for any value
img = cv2.imread('3.png',0)
img = cv2.bitwise_not(img)
img = cv2.resize(img,(28,28))
img = img/255
plt.imshow(img,cmap='gray')
plt.show()
img.shape

print(np.argmax(model.predict(np.array([img]))))
