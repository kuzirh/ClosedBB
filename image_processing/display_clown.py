import cv2 as cv
import sys


img = cv.imread("4825_PepeClown.png")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("4825_PepeClown.png", img)
if k == ord("q"):
    sys.exit("exiting the display window")