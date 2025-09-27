import cv2 

image = cv2.imread("opencv.png") 

cv2.imshow("original", image)   
cv2.waitKey(0)

b,g,r = cv2.split(image)

cv2.imshow("Blue saturation", b)
cv2.waitKey(0) 
cv2.imshow("Green saturation", g) 
cv2.waitKey(0) 
cv2.imshow("Red saturation", r) 





cv2.waitKey(0) 
cv2.destroyAllWindows()
