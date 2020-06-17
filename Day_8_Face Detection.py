import cv2
import matplotlib.pyplot as plt

# Get the image path and the xml path
img_path = r'C:\Users\ELCOT\Documents\Python Workouts_10 Day Training_Finland labs\faces.jpg'
xml_path = r'C:\Users\ELCOT\Documents\Python Workouts_10 Day Training_Finland labs\face.xml'

# Read the image
plt.figure(figsize = (7,7))
img = cv2.imread(img_path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# FACE DETECTION
#Haarcascade Classifier - Library for Face Detection
face_cascade = cv2.CascadeClassifier(xml_path)
faces = face_cascade.detectMultiScale(img)
print(faces)
print(len(faces))

# The array in len(face) has 16 elements and each element has four values. The values represents [x,y,w,h]
# (x,y) represents a co-ordinate, w represents the width of the image and h represents the height of the image
# Having all this data i can draw a rectangle by providing the diagonal elements. (x,y) and (x+w,y+h)

# EYE DETECTION
# It is easy to detect the eye from the face detected
eye_xml_path = r'C:\Users\ELCOT\Documents\Python Workouts_10 Day Training_Finland labs\eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_xml_path)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    single_face = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(single_face)
    for (ex,ey,eh,ew) in eyes:
        cv2.rectangle(single_face,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

plt.imshow(img)
plt.show()
