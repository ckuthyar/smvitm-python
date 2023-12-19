def collage1(college1,dept1):
    import cv2
    import numpy as np
    dim1=200
    dim2=300
    college=college1
    dept=dept1
    imgpath1="Images/"+college+"_"+dept+"/"
    imgpath2="Images/"+college+"_"+dept+"R"+"/"

    image1=cv2.imread(imgpath1+"1.jpg")
    image1=cv2.resize(image1,(dim1,dim2))
    image2=cv2.imread(imgpath1+"2.jpg")
    image2=cv2.resize(image2,(dim1,dim2))
    image3=cv2.imread(imgpath1+"3.jpg")
    image3=cv2.resize(image3,(dim1,dim2))
    image4=cv2.imread(imgpath1+"4.jpg")
    image4=cv2.resize(image4,(dim1,dim2))
    hstack1=np.hstack([image1,image2,image3,image4])
    cv2.imwrite(imgpath2+"Row1.jpg", hstack1)

    image1=cv2.imread(imgpath1+"5.jpg")
    image1=cv2.resize(image1,(dim1,dim2))
    image2=cv2.imread(imgpath1+"6.jpg")
    image2=cv2.resize(image2,(dim1,dim2))
    image3=cv2.imread(imgpath1+"7.jpg")
    image3=cv2.resize(image3,(dim1,dim2))
    image4=cv2.imread(imgpath1+"8.jpg")
    image4=cv2.resize(image4,(dim1,dim2))
    hstack1=np.hstack([image1,image2,image3,image4])
    cv2.imwrite(imgpath2+"Row2.jpg", hstack1)

    image1=cv2.imread(imgpath1+"9.jpg")
    image1=cv2.resize(image1,(dim1,dim2))
    image2=cv2.imread(imgpath1+"10.jpg")
    image2=cv2.resize(image2,(dim1,dim2))
    image3=cv2.imread(imgpath1+"11.jpg")
    image3=cv2.resize(image3,(dim1,dim2))
    image4=cv2.imread(imgpath1+"12.jpg")
    image4=cv2.resize(image4,(dim1,dim2))
    hstack1=np.hstack([image1,image2,image3,image4])
    cv2.imwrite(imgpath2+"Row3.jpg", hstack1)

    image1=cv2.imread(imgpath1+"13.jpg")
    image1=cv2.resize(image1,(dim1,dim2))
    image2=cv2.imread(imgpath1+"14.jpg")
    image2=cv2.resize(image2,(dim1,dim2))
    image3=cv2.imread(imgpath1+"15.jpg")
    image3=cv2.resize(image3,(dim1,dim2))
    image4=cv2.imread(imgpath1+"16.jpg")
    image4=cv2.resize(image4,(dim1,dim2))
    hstack1=np.hstack([image1,image2,image3,image4])
    cv2.imwrite(imgpath2+"Row4.jpg", hstack1)

    image1=cv2.imread(imgpath1+"17.jpg")
    image1=cv2.resize(image1,(dim1,dim2))
    image2=cv2.imread(imgpath1+"18.jpg")
    image2=cv2.resize(image2,(dim1,dim2))
    image3=cv2.imread(imgpath1+"19.jpg")
    image3=cv2.resize(image3,(dim1,dim2))
    image4=cv2.imread(imgpath1+"20.jpg")
    image4=cv2.resize(image4,(dim1,dim2))
    hstack1=np.hstack([image1,image2,image3,image4])
    cv2.imwrite(imgpath2+"Row5.jpg", hstack1)

    image1=cv2.imread(imgpath1+"21.jpg")
    image1=cv2.resize(image1,(dim1,dim2))
    image2=cv2.imread(imgpath1+"22.jpg")
    image2=cv2.resize(image2,(dim1,dim2))
    image3=cv2.imread(imgpath1+"23.jpg")
    image3=cv2.resize(image3,(dim1,dim2))
    image4=cv2.imread(imgpath1+"24.jpg")
    image4=cv2.resize(image4,(dim1,dim2))
    hstack1=np.hstack([image1,image2,image3,image4])
    cv2.imwrite(imgpath2+"Row6.jpg", hstack1)

    image1=cv2.imread(imgpath2+"Row1.jpg")
    image2=cv2.imread(imgpath2+"Row2.jpg")
    image3=cv2.imread(imgpath2+"Row3.jpg")
    image4=cv2.imread(imgpath2+"Row4.jpg")
    image5=cv2.imread(imgpath2+"Row5.jpg")
    image6=cv2.imread(imgpath2+"Row6.jpg")
    vstack1=np.vstack([image1,image2,image3,image4,image5,image6])
    cv2.imwrite(imgpath2+"Row123456.jpg",vstack1)
collage1("SMVITM","CS")


