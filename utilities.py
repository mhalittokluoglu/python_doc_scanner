import cv2
import numpy as np



def order_points(h):
    h = h.reshape((4,2))
    hnew = np.zeros((4,2), dtype = "float32")
    s = h.sum(1)
    hnew[0] = h[np.argmin(s)]
    hnew[2] = h[np.argmax(s)]
    diff = np.diff(h, axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]
    return hnew


def scan_image(image_str):
    img = cv2.imread(image_str)
    orig = img.copy()
    width_ratio = img.shape[1]/480
    height_ratio = img.shape[0]/640
    img = cv2.resize(img,(480,640))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(5,5),0)
    edged = cv2.Canny(blurred,30,50)
    contours,hierarchy = cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=cv2.contourArea,reverse = True)
    for c in contours:
        area = cv2.contourArea(c)
        if area> 1000:
            p = cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,0.02*p,True)
            if len(approx) == 4:
                target = approx
                break

    approx2 = order_points(target)
    approx3 = np.zeros((4,2), dtype = "float32")
    for i in range(0,4):
        approx3[i][0] = approx2[i][0]*width_ratio

    for i in range(0,4):
        approx3[i][1] = approx2[i][1]*height_ratio

    w1 = approx3[1][0] - approx3[0][0]
    w2 = approx3[2][0] - approx3[3][0]
    wdth = max(w1,w2)

    h1 = approx3[3][1] - approx3[0][1]
    h2 = approx3[2][1] - approx3[1][1]
    hgth = max(h1,h2)

    pts1 = np.float32([[0,0],[wdth,0],[wdth,hgth],[0,hgth]])
    op = cv2.getPerspectiveTransform(approx3,pts1)
    dst = cv2.warpPerspective(orig,op,(int(wdth),int(hgth)))
    return dst
