# video capture open cv
import cv2
cap = cv2.VideoCapture(0);
while(True):
 ret, frame = cap.read()
 cv.imshow('frame',frame)
 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
cap.release()
cv2.destroyAllWindows()
