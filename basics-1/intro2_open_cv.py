import cv2 

image = cv2.imread("pika.png", 0) 

cv2.imshow("grayscale", image) 


cv2.imwrite("C:/Users/aruni/Downloads/gray_pika.png", image) 





cv2.waitKey(0)
cv2.destroyAllWindows()