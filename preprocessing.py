

import cv2
 
# colored Image
# Img = cv2.imread (“Penguins.jpg”,1)

# Black and White (gray scale) 
Img = cv2.imread (“Penguins.jpg”,0)
 
# displaying an image

cv2.imshow(“Penguins”, img)
 
cv2.waitKey(0)


#resizing an image

resized_image = cv2.resize(img, (650,500))
# Resized_image = cv2.resize(img, int(img.shape[1]/2), int(img.shape[0]/2)))
 
cv2.imshow(“Penguins”, resized_image)
 
cv2.waitKey(2000)
 
cv2.destroyAllWindows()



