import cv2 #import the main module

img = cv2.imread("pika.png") #"reading an image" 

#converting a coloured image into a grayscale image

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow("gray_pikachu", gray_image)
cv2.waitKey(0)


cv2.imshow("pikachu", img) #displaying an image: 1st parameter = the title 2nd is the image
cv2.waitKey(0) 
cv2.destroyAllWindows()