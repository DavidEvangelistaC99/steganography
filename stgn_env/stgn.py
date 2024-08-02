import cv2
import numpy as np
import hiding
import read

data_send = "The Canny filter is a widely used edge detection algorithm in computer vision, developed by John F. Canny in 1986. It is a multi-stage algorithm that detects a wide range of edges in images, including lines, curves, and corners. The Canny filter is known for its ability to effectively detect edges while reducing noise and false positives."

##---Hiding Data---##
hiding.hiding_text(data_send,"vegetable_in.png")