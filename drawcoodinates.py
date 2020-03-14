import cv2
import sys
import numpy as np

drawing = False 
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):

    global ix,iy,drawing,arr_point

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_LBUTTONUP:

        drawing = False
        cv2.circle(img,(x,y),4,(0,0,255),-1)
        arr_point.append([x,y])
    
def delete_point():

    global arr_point,img

    if len(arr_point) == 0:
        print("return")
        return
    else:
        arr_point.pop(-1)
        cv2.destroyAllWindows()
        img = cv2.imread("image.jpg")
        cv2.namedWindow('image')
        
        for i in range(0,len(arr_point)):
            x=arr_point[i][0]
            y=arr_point[i][1]
            cv2.circle(img,(x,y),4,(0,0,255),-1)
        cv2.setMouseCallback('image',draw_circle) 

arr_point=[]
img = cv2.imread(sys.argv[1])
cv2.imwrite("image.jpg", img)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 100:
        print("press delete")
        delete_point()
    if k == 27:
        file_object = open("coordinate.txt","w")
        for i in range(0,len(arr_point)):
            x = str(arr_point[i][0])
            y = str(arr_point[i][1])
            print(x,y)
            file_object.write(x+" "+y+'\n')
        file_object.close()    
        break
cv2.destroyAllWindows()   