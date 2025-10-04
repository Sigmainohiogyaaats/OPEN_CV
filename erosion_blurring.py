import cv2 
import numpy as np

"""img = cv2.imread("pika.png") 
kernel = np.ones((1,1), np.uint8) 

eroded = cv2.erode(img, kernel)



cv2.imshow("My image", img)  
cv2.waitKey(0) 
cv2.imshow("eroded image", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows() """

img = cv2.imread("pika.png") 
#Gaussian Blur
blurred = cv2.GaussianBlur(img , (15,15), 0)
#Median Blur 
median = cv2.medianBlur(img, 5)
#bilateral filter 
bilateral = cv2.bilateralFilter(img, 9,75,75) 

cv2.imshow("My image", img)  
cv2.waitKey(0)
cv2.imshow("Blurred_img", blurred) 
cv2.waitKey(0)
cv2.imshow("Median_Blur", median) 
cv2.waitKey(0)
cv2.imshow("Bilateral", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()