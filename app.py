import cv2
original_image = cv2.imread("khurram.jpg")
gray_scaled = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
image_inverted = 255 - gray_scaled
blurred_image = cv2.GaussianBlur(image_inverted, (25, 25), 0)
blurred_inverted = 255 - blurred_image
sketch_effect = cv2.divide(gray_scaled, blurred_inverted, scale=240.0)
cv2.imwrite("unique_sketch_image.png", sketch_effect)
cv2.imshow("Pencil Sketch Effect", sketch_effect)
cv2.waitKey(0)
cv2.destroyAllWindows()




