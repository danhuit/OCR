import cv2
import sys
import tesseract
import pytesseract

def crop_image(image, arr_coodinates):

    crop_img = image[arr_coodinates[0][1]:arr_coodinates[1][1], arr_coodinates[0][0]:arr_coodinates[1][0]]
    
    return crop_img


def ocr_process(image, arr_coodinates):
    # process images by coodinates 

    crop_img = crop_image(image, arr_coodinates)
    print(pytesseract.image_to_string(cv2.imread("out.jpg"), lang='fra'))
    result=[]
    return result

def get_coodinates():
    # get coodinates get from gui

    result=[]

    with open('coordinate.txt') as f:

        w, h = [int(x) for x in next(f).split()]
        array = [[int(x) for x in line.split()] for line in f]
        result.append([w,h])
        result.append(array[0])

    return result

if __name__ == "__main__":

    # read image
    image = cv2.imread(str(sys.argv[1]))
    
    # get coodinates from gui
    arr_coodinates = get_coodinates()

    # process ocr
    result = ocr_process(image, arr_coodinates)
    #print("result ocr: ", result)

