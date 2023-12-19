
import cv2
import numpy as np
image1=cv2.imread("Images/SMVITM_EC/1.jpg")
image1=cv2.resize(image1,(100,150))
image2=cv2.imread("Images/SMVITM_EC/2.jpg")
image2=cv2.resize(image2,(100,150))
image3=cv2.imread("Images/SMVITM_EC/3.jpg")
image3=cv2.resize(image3,(100,150))

hstack1=np.hstack([image1,image2,image3])
cv2.imwrite("Images/SMVITM_ECR/Row1.jpg", hstack1)


