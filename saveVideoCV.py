#code for saving video

import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.cv.CV_FOURCC(*'XVID')

#fourcc= cv2.VideoWriter_fourcc(*'XVID') used for cv3/ cv4 

out = cv2.VideoWriter('output.avi',fourcc,24.0,(640,480))

print(cap.isOpened())

while(cap.isOpened()):

 ret,frame = cap.read()

 if ret == True: 
    print(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

    out.write(frame)

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
 
    if cv2.waitKey(1) & 0xFF==ord('q'):
      break
 
 else:
      break

cap.release()
out.release()
cv2.destroyAllWindows()
