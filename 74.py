
import cv2
import numpy as np
dim1=200
dim2=300

image1=cv2.imread("Images/SMVITM_EC/1.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_EC/2.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_EC/3.jpg")
image3=cv2.resize(image3,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3])
cv2.imwrite("Images/SMVITM_ECR/Row1.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_EC/4.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_EC/5.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_EC/6.jpg")
image3=cv2.resize(image3,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3])
cv2.imwrite("Images/SMVITM_ECR/Row2.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_EC/7.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_EC/8.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_EC/9.jpg")
image3=cv2.resize(image3,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3])
cv2.imwrite("Images/SMVITM_ECR/Row3.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_EC/10.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_EC/11.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_EC/12.jpg")
image3=cv2.resize(image3,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3])
cv2.imwrite("Images/SMVITM_ECR/Row4.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_EC/13.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_EC/14.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_EC/15.jpg")
image3=cv2.resize(image3,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3])
cv2.imwrite("Images/SMVITM_ECR/Row5.jpg", hstack1)


image1=cv2.imread("Images/SMVITM_ECR/Row1.jpg")
image2=cv2.imread("Images/SMVITM_ECR/Row2.jpg")
image3=cv2.imread("Images/SMVITM_ECR/Row3.jpg")
image4=cv2.imread("Images/SMVITM_ECR/Row4.jpg")
image5=cv2.imread("Images/SMVITM_ECR/Row5.jpg")
vstack1=np.vstack([image1,image2,image3,image4,image5])
cv2.imwrite("Images/SMVITM_ECR/Row12345.jpg",vstack1)



