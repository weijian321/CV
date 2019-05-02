#!/usr/bin/env python
# coding: utf-8

#    Finish 2D convolution/filtering by your self.
#    What you are supposed to do can be described as "median blur", which means by using a sliding window
#    on an image, your task is not going to do a normal convolution, but to find the median value within
#    that crop.
#
#    You can assume your input has only one channel. (a.k.a a normal 2D list/vector)
#    And you do need to consider the padding method and size. There are 2 padding ways: REPLICA & ZERO. When
#    "REPLICA" are given to you, the padded pixels are the same with the border pixels. E.g is [1 2 3] is your
#    image, the padded version will be [(...1 1) 1 2 3 (3 3...)] where how many 1 & 3 in the parenthesis
#    depends on your padding size. When "ZERO", the padded version will be [(...0 0) 1 2 3 (0 0...)]

#    def medianBlur(img, kernel, padding_way):
#        img & kernel is List of List; padding_way a string
#        Please finish your code under this blank
import numpy as np
import cv2

def medianBlur(img, kernel, padding_way,padding_size=2):
    img_padded=[]
    h,w=img.shape
    kh,kw=kernel.shape
    if padding_way == 'REPLICA':
        img_padded = np.pad(img, padding_size, 'edge')
    elif padding_way == 'ZERO':
        img_padded = np.pad(img, padding_size, 'constant')
    print(img_padded)
    cv2.imshow(padding_way, img_padded)
    out_h, out_w = (h+2*padding_size+1-kh), (w+2*padding_size+1-kw)
    img_pooling = np.zeros((out_h, out_w))
    for i in range(out_h):
        for j in range(out_w):
            img_pooling[i][j] = np.median(img_padded[i:i+kh, j:j+kw])
    return img_pooling




if  __name__=='__main__':
    img_gray = cv2.imread('lena.jpg', 0)
    kernel = cv2.getGaussianKernel(5, 1)
    kernel2D = kernel*kernel.T
    # a = np.array([[1, 2, 3], [5, 6, 7], [8, 9, 10]])
    # print(a[0:3, 1:3])
    # print(np.median(a[0:3, 1:3]))
    # img_gray=np.arange(1,17).reshape(4,4)
    # kernel2D=np.arange(1,5).reshape(2,2)
    print(img_gray.shape)
    print(kernel2D.shape)
    img_padding_REPLICA = medianBlur(img_gray, kernel2D, 'REPLICA')
    print(img_padding_REPLICA.shape)
    print('img_padding_REPLICA:\r\n', img_padding_REPLICA)
    print('img_gray dtype:\r\n', img_gray.dtype)
    print('img_padding_REPLICA dtype:\r\n', img_padding_REPLICA.dtype)
    img_padding_ZERO = medianBlur(img_gray, kernel2D, 'ZERO')
    print(img_padding_ZERO.shape)

    cv2.imshow('img_padding_REPLICA', np.uint8(img_padding_REPLICA))
    cv2.imshow('img_padding_ZERO', np.uint8(img_padding_ZERO))
    print(img_padding_ZERO.shape)
    key=cv2.waitKey()
    if key == 27:
        cv2.destroyAllWindows()
