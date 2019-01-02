import cv2
import numpy as np



img1 = cv2.imread('/Users/yangxiaoyu/Desktop/RMB/100.jpg')


img2=cv2.resize(img1,(1000,500),interpolation=cv2.INTER_CUBIC)


img = cv2.GaussianBlur(img2, (5,5),0)

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)

absX = cv2.convertScaleAbs(x)   # 转回uint8
absY = cv2.convertScaleAbs(y)

img = cv2.addWeighted(absX,0.5,absY,0.5,0)


ret,dst=cv2.threshold(img,110,255,cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

#开闭运算，先开运算去除背景噪声，再继续闭运算填充目标内的孔洞
# opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)


_,contours, hierarchy = cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#绘制轮廓
# cv2.drawContours(img2,contours,-1,(0,0,255),3)


save = []  #存储合理轮廓
rectall = []  #存储对应的在最小面积矩形



for i in range(len(contours)):
    if(0<cv2.contourArea(contours[i])<7000):
            save.append(contours[i])



for i in range(0,len(save)):
    x, y, w, h = cv2.boundingRect(save[i])

    cv2.rectangle(img2, (x,y), (x+w,y+h), (153,153,0), 5)


# for contour in contours:
#     rect = cv2.minAreaRect(contour)
#     if verifySizes(rect):
#         save.append(contour)
#
cv2.drawContours(img2,save,-1,(0,0,255),2)

# print(save)
cv2.imshow('bb', closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
