# coverting video to gray 
#get width and height using cap.get(cv2.cv.CV_CAP_PROP_ )) method



import cv2
cap = cv2.VideoCapture(0);
while(True)
 ret, frame=cap.read()
 print(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
 print(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
 
 gray = cv2.cvt_color(frame,cv2.COLOR_BGR2GRAY)
 
 cv2.imshow('frame',gray)
 if cv2.waitKey(0) & 0xFF == ord('q')
  break
cv2.release()
cv2.destroyAllWindows()
  

 
