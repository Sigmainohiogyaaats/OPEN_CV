import cv2 

image = cv2.imread("pika.png") 

cv2.imshow("original", image) 
cv2.waitKey(0)

resized_image = cv2.resize(image, (300, 300)) 
cv2.imshow("resized", resized_image)

#adding a border 
border_solid = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value = 3) #border constant is the algorithm that is used for designing the border. 
#reflective border 
reflect = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_REFLECT) 
#Wrap Border 
wrap = cv2.copyMakeBorder(image, 50, 50, 50, 50,cv2.BORDER_WRAP)


cv2.imshow("Solid Border", border_solid)
cv2.waitKey(0)
cv2.imshow("Reflective _border", reflect)
cv2.waitKey(0) 
cv2.imshow("wrap_border", wrap) 
cv2.waitKey(0)
cv2.destroyAllWindows() 


