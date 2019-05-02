# coding=utf8

import cv2
import numpy as np

img = cv2.imread('lena.jpg')
img_gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

g_img = cv2.GaussianBlur(img, (7, 7), 1)
cv2.imshow('lena_Gaussian', g_img)

kernel = cv2.getGaussianKernel(7, 1)
g2_img = cv2.sepFilter2D(img, -1, kernel, kernel)
cv2.imshow('lena_Gaussian_kernel', g2_img)

kernel_lap = np.array([[0,1,0],[1,-3,1],[0,1,0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_lap)
cv2.imshow('lena_lap', lap_img)

kernel_sharp = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)
sharp_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('lena_sharp', sharp_img)

kernel_edgex = np.array([[-1,-2,-1],[0,0,0],[1,2,1]], np.float32)
edgex_img = cv2.filter2D(img, -1, kernel=kernel_edgex)
cv2.imshow('lena_edgex', edgex_img)

kernel_edgey = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], np.float32)
edgey_img = cv2.filter2D(img, -1, kernel=kernel_edgey)
cv2.imshow('lena_edgey', edgey_img)

img_harris = cv2.cornerHarris(img_gray, 2, 3, 0.05)
thres = 0.05 * np.max(img_harris)
img[img_harris > thres] = [0, 0, 255]
cv2.imshow('lena', img)

########### SIFT ###########
img = cv2.imread('lena.jpg')
# create sift class
sift = cv2.xfeatures2d.SIFT_create()
# detect SIFT
print('sift:{}\r\n'.format(sift))
print('sift_type:{}\r\n'.format(type(sift)))
kp = sift.detect(img, None)   # None for mask
print('kp:{}\r\n'.format(kp))
print('kp_type:{}\r\n'.format(type(kp)))
# compute SIFT descriptor
kp,des = sift.compute(img, kp)
a = np.array([1, 2, 3, 4])
print(a.shape)
img_sift = cv2.drawKeypoints(img, kp, outImage=np.array([]), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('lenna_sift.jpg', img_sift)

key = cv2.waitKey()
if key == 27:
    cv2.destroyAllwindows()




