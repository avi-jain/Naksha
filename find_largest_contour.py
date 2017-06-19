import numpy as np
import cv2
import matplotlib.pyplot as plt

def find_biggest_contour(image):
	# Copy because contours modifies og image
	image_cp = image.copy()
	clone = cv2.Canny(image_cp,100,200,apertureSize = 3)
	clone = cv2.GaussianBlur(clone,(5,5),0)
	plt.imshow(clone, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()

	#gives all the contours, contour approximation, if applied, compresses horizontal, 
	#vertical, and diagonal segments and leaves only their end points.
	#Optional output vector, containing information about the image topology. 
	#It has as many elements as the number of contours.
	# Chain approx = None so that we can extract the whole shape as an array
	# Also, this doesn't support 3 channel images
	#image_mod, contours, hierarchy = cv2.findContours(image_cp, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
	image_mod, contours, hierarchy = cv2.findContours(clone, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

	# Isolate largest contour
	contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
	biggest_contour_size = max(contour_sizes, key=lambda x: x[0])[0]
	print biggest_contour_size
	biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
	print biggest_contour.shape
	
	mask = np.zeros(image.shape, np.uint8)
	#first argument is source image
	#second argument is the contours which should be passed as a Python list 
	#third argument is index of contours. -1 draws all contours
	# cv2.drawContours(image_cp, [biggest_contour], -1, (0,0,255), 3)
	# Draw the largest contour and fill with white
	mask = cv2.drawContours(mask, [biggest_contour], -1, (255,255,255), cv2.FILLED)
	return biggest_contour, mask

rgb_image = cv2.imread('test2.jpg')
image = cv2.cvtColor(rgb_image,cv2.COLOR_RGB2GRAY)

plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
biggest_contour, mask = find_biggest_contour(image)

mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
result = np.zeros(rgb_image.shape, np.uint8)  
result = np.where(mask == 0, result, rgb_image)  # set everything where the mask is white to the value of og image

# plt.imshow(mask, cmap = 'gray', interpolation = 'bicubic')
# below for blue-red, above for black and white
plt.imshow(result, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

#plt.imshow(mask, interpolation = 'bicubic')
#plt.imsave("edited",mask)
#cv2.imwrite('messigray.png',img)