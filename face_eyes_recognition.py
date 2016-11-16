"""
face and eye recognition in videos using haar cascades
"""

import cv2
import numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#cap = cv2.VideoCapture(0) #capture video from cam
cap = cv2.VideoCapture('/Users/kanna/Downloads/TrumpFaces.mp4') #input video from file
#cap = cv2.VideoCapture('/Users/kanna/Downloads/ThalaivarAnnamalai1.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#out = cv2.VideoWriter('output.mp4', fourcc, 8, (width*2, height*2))
out = cv2.VideoWriter('output.mp4', fourcc, 30, (width, height))

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex, ey, ew, eh) in eyes:
        #    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

    cv2.imshow('img', img)
    out.write(img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
