"""
imageTset02 -

Author: 12551
Date: 2022/7/17
"""
import cv2

image_Color = cv2.imread("12.jpg")
print("获取彩色图像的属性")
print("shape", image_Color.shape)
print(image_Color.size)
print(image_Color.dtype)
print("================")
image_Gray = cv2.imread("12.jpg", 0)
print("shape", image_Gray.shape)
print(image_Gray.size)
print(image_Gray.dtype)
