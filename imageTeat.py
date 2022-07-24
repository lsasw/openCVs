"""
imageTeat -

Author: 12551
Date: 2022/7/16
"""
import cv2

image = cv2.imread("12.jpg")
cv2.imwrite("E:/python/openCVs/image/13.jpg", image)  # 这里需要加上，一个文件名要不然，电脑不知道
cv2.imshow("blackboard", image)  # 中文名会报错
cv2.waitKey(5000)  # 1000ms为1s
cv2.destroyAllWindows()
