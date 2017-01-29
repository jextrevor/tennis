import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

boundaries = [
	([51, 169, 144], [151, 269, 244]),
]
#BGR order

for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 	gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
 	cv2.imshow("output", np.hstack([image, output]))
 	cv2.waitKey(0)
# ensure at least some circles were found
	if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
		cv2.imshow("output", np.hstack([image, output]))
		cv2.waitKey(0)