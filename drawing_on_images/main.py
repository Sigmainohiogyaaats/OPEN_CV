import cv2 


img = cv2.imread("hritik.png") 

# drawing a line 
start = (50,50) 
end = (350,50) 
line_color = (132, 146,30) 
line_thickness = 3
#drawing the line
cv2.line(img, start, end, line_color, line_thickness)

# drawing a rectangle 
top_left = (450,300)
bottom_right = (550,400)
line_thickness = 2

cv2.rectangle(img,top_left, bottom_right,line_color, line_thickness)

#drawing a circle 
center = (490,600) 
radius = 100
line_thickness = -1 

cv2.circle(img, center, radius, line_color, line_thickness) 
cv2.circle(img, center, 80, (67,80,90), -1)
cv2.circle(img, center, 50, (120,80,90), -1) 
cv2.circle(img, center, 35, (180,80,90), -1) 

#drawing an ellipse

center = (495,200)
axes = (100,50) 
angle = 0 
thickness = 2

cv2.ellipse(img, center, axes, angle,startAngle=0, endAngle=360, color = (180,90,80), thickness = -1)


cv2.imshow("Hritik", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()