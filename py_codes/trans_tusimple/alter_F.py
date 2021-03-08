import glob
import os
from PIL import Image
import matplotlib.pyplot as plt
import cv2
img_path = glob.glob("C:/Users/bcl/Desktop/image/*.jpg")
num = 1
for file in img_path:
  img = cv2.imread(file)
  # plt.imshow(img)
  # plt.show()
  img1 = cv2.resize(img,(1280,720),interpolation = cv2.INTER_AREA)
  cv2.imwrite("C:/Users/bcl/Desktop/1/"+ str(num) + ".jpg",img1)
  num = num + 1




