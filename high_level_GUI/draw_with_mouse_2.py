#!/usr/bin/python3

import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
radius = 3
color = (0,255,0)
thickness = -1
pressed = False

# click callback
def click(event, x, y, flags, param):
	global canvas, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		pressed = True
		cv2.circle(canvas,(x,y),radius,color,thickness)
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
		cv2.circle(canvas,(x,y),radius,color,thickness)
	elif event == cv2.EVENT_LBUTTONUP:
		pressed = False

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	# if 'q' then quit the program
	if ch & 0xFF == ord('q'):
		break
	# if 'b' then change color to blue
	elif ch & 0xFF == ord('b'):
		color = (255,0,0)
	# if 'g' then change color to green
	elif ch & 0xFF == ord('g'):
		color = (0,255,0)
	# if 'r' then change color to red
	elif ch & 0xFF == ord('r'):
		color = (0,0,255)
	
	

cv2.destroyAllWindows()