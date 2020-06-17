
# How to display image in separate window

# import cv2
# img_path = r'C:\Users\ELCOT\Documents\Python Workouts_10 Day Training_Finland labs\faces.jpg'
# img = cv2.imread(img_path)
# cv2.imshow('Faces',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Access Webcam
import cv2

# For face detection
xml_path = r'C:\Users\ELCOT\Documents\Python Workouts_10 Day Training_Finland labs\face.xml'
face_cascade = cv2.CascadeClassifier(xml_path)

# For Eye detection
eye_xml_path = r'C:\Users\ELCOT\Documents\Python Workouts_10 Day Training_Finland labs\eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_xml_path)

cam = cv2.VideoCapture(0) # The 0 argument means open the webcam in system
while True:
    ret,img = cam.read() # img will be having continuous images and ret is a boolean value, if the image is captured ret is true, else it is false
    faces = face_cascade.detectMultiScale(img,1.2)
    count = "No.of.faces - "  + str(len(faces))
    cv2.putText(img,count,(100,100),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        single_face = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(single_face)
        for (ex,ey,eh,ew) in eyes:
             cv2.rectangle(single_face,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == 13:  # 13 is the ascii code for enter
        break
cam.release()
cv2.destroyAllWindows()

# Detect object by colour
# To detect the image by colour, firstwe have to convert the image to hue saturation value

import cv2
import numpy as np 
cam = cv2.VideoCapture(0)
while True:
    ret,img = cam.read()
    hsv  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # Red Colour
    low = np.array([140,150,0])
    high = np.array([180,255,255])
    img_mask = cv2.inRange(hsv,low,high)
    output = cv2.bitwise_and(img,img,mask = img_mask) # To display the white portion as red colour
    cv2.imshow("Output",output)
    cv2.imshow("HSV", hsv)
    cv2.imshow('Webcam', img)
    cv2.imshow("Mask",img_mask)
    if cv2.waitKey(1) == 13: 
        break
cam.release()
cv2.destroyAllWindows()



