import cv2
img = cv2.imread('picpy.jpg',0)
print(img)
cv.imshow('PicWindow',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('pic_copy.png',img)

