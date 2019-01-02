#-*- coding: UTF-8 -*-


import operator
import cv2
import numpy as np
from PIL import Image
import imagehash


def get_image(path):
    #获取图片
    img=cv2.imread(path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    return img, gray

def Gaussian_Blur(gray):
    # 高斯去噪
    blurred = cv2.GaussianBlur(gray, (3, 3),0)

    return blurred

def Erzi(blurred):
    ret,thresh1=cv2.threshold(blurred,130,255,cv2.THRESH_BINARY)
    return thresh1

def Sobel_gradient(blurred):
    # 索比尔算子来计算x、y方向梯度
    gradX = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=1, dy=0)
    gradY = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=0, dy=1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    return gradX, gradY, gradient

def Thresh_and_blur(gradient):

    blurred = cv2.GaussianBlur(gradient, (9, 9), 0)
    (_, thresh) = cv2.threshold(blurred, 106, 255, cv2.THRESH_BINARY)

    return thresh

def image_morphology(thresh):

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=3)
    closed = cv2.dilate(closed, None, iterations=3)

    return closed

def findcnts_and_box_point(closed):

    (_, cnts, _) = cv2.findContours(closed.copy(),
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    return box

def drawcnts_and_cut(original_img, box):
    draw_img = cv2.drawContours(original_img.copy(), [box], -1, (0, 0, 255), 3)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    hight = y2 - y1
    width = x2 - x1
    crop_img = original_img[y1:y1+hight, x1:x1+width]

    return draw_img, crop_img

def walk():

    img_path = r'C:/Users/yxy86/Desktop/RMB/23.jpg'

    save_path = r'C:/Users/yxy86/Desktop/RMB/01/mtest.jpg'
    original_img, gray = get_image(img_path)
    blurred = Gaussian_Blur(gray)
    th1 = Erzi(blurred)
    gradX, gradY, gradient = Sobel_gradient(th1)
    thresh = Thresh_and_blur(gradient)
    closed = image_morphology(thresh)
    box = findcnts_and_box_point(closed)
    draw_img, crop_img = drawcnts_and_cut(original_img,box)

    # 暴力一点，把它们都显示出来看看

    # cv2.imshow('original_img', original_img)
    # cv2.imshow('blurred', blurred)
    # cv2.imshow('gradX', gradX)
    # cv2.imshow('gradY', gradY)
    # cv2.imshow('final', gradient)
    # cv2.imshow('thresh', thresh)
    # cv2.imshow('closed', closed)
    # cv2.imshow('draw_img', draw_img)
    # cv2.imshow('crop_img', crop_img)
    # cv2.waitKey(0)
    cv2.imwrite(save_path, crop_img)



def hist(path):
    img=cv2.imread(path,0)
    hist=cv2.calcHist([img],[0],None,[256],[0,256])
    return hist

def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

def make_regalur_image(img, size = (256, 256)):
    return img.resize(size).convert('RGB')


def calc_similar(li, ri):
    return hist_similar(li.histogram(), ri.histogram())



path1 = 'C:/Users/yxy86/Desktop/RMB/m1.jpg'
path5 ='C:/Users/yxy86/Desktop/RMB/m5.jpg'
path10 = 'C:/Users/yxy86/Desktop/RMB/m10.jpg'
path20='C:/Users/yxy86/Desktop/RMB/m20.jpg'
path50 = 'C:/Users/yxy86/Desktop/RMB/m50.jpg'
path100 = 'C:/Users/yxy86/Desktop/RMB/m100.jpg'

pathm = 'C:/Users/yxy86/Desktop/RMB/01/mtest.jpg'


def calc(path1,path2):
    img1 = Image.open(path1)
    img2 = Image.open(path2)
    img1 = make_regalur_image(img1)
    img2 = make_regalur_image(img2)
    return calc_similar(img1,img2)

dict1 = {'100': '', '50':' ', '20':'', '10': '', '5': '', '1':''}


walk()
dict1['100'] = calc(pathm,path100)
dict1['50'] = calc(pathm,path50)
dict1['20'] = calc(pathm,path20)
dict1['10'] = calc(pathm,path10)
dict1['5'] = calc(pathm,path5)
dict1['1'] = calc(pathm,path1)


hist = hist('C:/Users/yxy86/Desktop/RMB/mtest.jpg')


dif = 0
max = 100




# def hammingDistance( x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         return bin(x ^ y).count('1')

save = []
sorted_x=sorted(dict1.items(),key=operator.itemgetter(1))
# print(sorted_x[sorted_x.keys():tuple[-1]])
print(list(dict(sorted_x).keys())[-1])







