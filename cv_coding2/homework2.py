# Homework Week 2:
#
# 1. 【Coding】:
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
#
#    Assume your input's size of the image is W x H, kernel size's m x n. You may first complete a version
#    with O(W·H·m·n log(m·n)) to O(W·H·m·n·m·n)).
#    Follow up 1: Can it be completed in a shorter time complexity?
#    Follow up 2: Can it be completed in O(W·H·m·n)?
#
#    Python version:
#    def medianBlur(img, kernel, padding_way):
#        img & kernel is List of List; padding_way a string
#        Please finish your code under this blank
#
#
#//   C++ version:
#//   void medianBlur(vector<vector<int>>& img, vector<vector<int>> kernel, string padding_way){
#//       Please finish your code within this blanck  
#//   }
#
#    We recommend to try in both language (Especially in C++).
#    Good Luck!

#    2. 【Reading + Pseudo Code】
#       We haven't told RANSAC algorithm this week. So please try to do the reading.
#       And now, we can describe it here:
#       We have 2 sets of points, say, Points A and Points B. We use A.1 to denote the first point in A, 
#       B.2 the 2nd point in B and so forth. Ideally, A.1 is corresponding to B.1, ... A.m corresponding 
#       B.m. However, it's obvious that the matching cannot be so perfect and the matching in our real
#       world is like: 
#       A.1-B.13, A.2-B.24, A.3-x (has no matching), x-B.5, A.4-B.24(This is a wrong matching) ...
#       The target of RANSAC is to find out the true matching within this messy.
#       
#       Algorithm for this procedure can be described like this:
#       1. Choose 4 pair of points randomly in our matching points. Those four called "inlier" (中文： 内点) while 
#          others "outlier" (中文： 外点)
#       2. Get the homography of the inliers
#       3. Use this computed homography to test all the other outliers. And seperated them by using a threshold 
#          into two parts:
#          a. new inliers which is satisfied our computed homography
#          b. new outliers which is not satisfied by our computed homography.
#       4. Get our all inliers (new inliers + old inliers) and goto step 2
#       5. As long as there's no changes or we have already repeated step 2-4 k, a number actually can be computed,
#          times, we jump out of the recursion. The final homography matrix will be the one that we want.
#
#       [WARNING!!! RANSAC is a general method. Here we add our matching background to that.]
#
#       Your task: please complete pseudo code (it would be great if you hand in real code!) of this procedure.
#
#       Python:
#       def ransacMatching(A, B):
#           A & B: List of List
#
#//     C++:
#//     vector<vector<float>> ransacMatching(vector<vector<float>> A, vector<vector<float>> B) {
#//     }     
#
#       Follow up 1. For step 3. How to do the "test“? Please clarify this in your code/pseudo code
#       Follow up 2. How do decide the "k" mentioned in step 5. Think about it mathematically!
#
#       3. 【Projects】:
#       We describe this in another section.          

import numpy as np
n_samples = 500  # 样本个数
n_inputs = 1  # 输入变量个数
n_outputs = 1  # 输出变量个数
A_exact = 20 * np.random.random((n_samples, n_inputs))  # 随机生成0-20之间的500个数据:行向量
print('A_exact:\r\n',A_exact)
perfect_fit = np.random.normal(size=(1000000*n_inputs, 100*n_outputs))  # 随机线性度即随机生成一个斜率
print('perfect_fit:\r\n', perfect_fit[perfect_fit > 5])
