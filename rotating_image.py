import cv2 
#specific degree rotation
img = cv2.imread("pika.png")  
(row,column) = img.shape [:2] 
#print(row,column)  

metric = cv2.getRotationMatrix2D((column//2, row//2), 45,1) 
rotated_image = cv2.warpAffine(img, metric, (column,row))

cv2.imshow("My image", img) 
cv2.imshow("rotation", rotated_image)
cv2.waitKey(0)

#basic rotation(90,180,270)
img = cv2.imread("pika.png") 

rotation90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 

cv2.imshow("rotated", rotation90) 

cv2.waitKey(0) 
cv2.destroyAllWindows()

