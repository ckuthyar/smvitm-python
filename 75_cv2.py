
import cv2
import numpy as np
dim1=200
dim2=300

image1=cv2.imread("Images/SMVITM_CS/1.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_CS/2.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_CS/3.jpg")
image3=cv2.resize(image3,(dim1,dim2))
image4=cv2.imread("Images/SMVITM_CS/4.jpg")
image4=cv2.resize(image4,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3,image4])
cv2.imwrite("Images/SMVITM_CSR/Row1.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_CS/5.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_CS/6.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_CS/7.jpg")
image3=cv2.resize(image3,(dim1,dim2))
image4=cv2.imread("Images/SMVITM_CS/8.jpg")
image4=cv2.resize(image4,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3,image4])
cv2.imwrite("Images/SMVITM_CSR/Row2.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_CS/9.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_CS/10.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_CS/11.jpg")
image3=cv2.resize(image3,(dim1,dim2))
image4=cv2.imread("Images/SMVITM_CS/12.jpg")
image4=cv2.resize(image4,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3,image4])
cv2.imwrite("Images/SMVITM_CSR/Row3.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_CS/13.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_CS/14.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_CS/15.jpg")
image3=cv2.resize(image3,(dim1,dim2))
image4=cv2.imread("Images/SMVITM_CS/16.jpg")
image4=cv2.resize(image4,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3,image4])
cv2.imwrite("Images/SMVITM_CSR/Row4.jpg", hstack1)

image1=cv2.imread("Images/SMVITM_CS/17.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_CS/18.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_CS/19.jpg")
image3=cv2.resize(image3,(dim1,dim2))
image4=cv2.imread("Images/SMVITM_CS/20.jpg")
image4=cv2.resize(image4,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3,image4])
cv2.imwrite("Images/SMVITM_CSR/Row5.jpg", hstack1)


image1=cv2.imread("Images/SMVITM_CS/21.jpg")
image1=cv2.resize(image1,(dim1,dim2))
image2=cv2.imread("Images/SMVITM_CS/22.jpg")
image2=cv2.resize(image2,(dim1,dim2))
image3=cv2.imread("Images/SMVITM_CS/23.jpg")
image3=cv2.resize(image3,(dim1,dim2))
image4=cv2.imread("Images/SMVITM_CS/24.jpg")
image4=cv2.resize(image4,(dim1,dim2))
hstack1=np.hstack([image1,image2,image3,image4])
cv2.imwrite("Images/SMVITM_CSR/Row6.jpg", hstack1)


image1=cv2.imread("Images/SMVITM_CSR/Row1.jpg")
image2=cv2.imread("Images/SMVITM_CSR/Row2.jpg")
image3=cv2.imread("Images/SMVITM_CSR/Row3.jpg")
image4=cv2.imread("Images/SMVITM_CSR/Row4.jpg")
image5=cv2.imread("Images/SMVITM_CSR/Row5.jpg")
image6=cv2.imread("Images/SMVITM_CSR/Row6.jpg")
vstack1=np.vstack([image1,image2,image3,image4,image5,image6])
cv2.imwrite("Images/SMVITM_CSR/Row123456.jpg",vstack1)



