# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2 
  
vid = cv2.VideoCapture(0) 
#img = cv2.VideoCapture(0)
  
while(True): 
      
    ret, frame = vid.read() 
    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

#ret, img2 = img.read()
#cv2.imshow('Image from Camera', img2)
#cv2.imwrite("CameraImage.png", img2)
vid.release() 
cv2.destroyAllWindows() 