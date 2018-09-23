import cv2
import numpy as np
# from matplotlib import pyplot as plt
# from PIL import Image
#from scipy import misc as smp
# from scipy import signal
# import PIL



def CompereHistograms(img1,img2):
    """Indication if the images equal """
    #image1 = cv2.imread(img1)
    #image2 = cv2.imread(img2)
    ValRGB = 0
    for i in range(0,3):
        histr1 = cv2.calcHist([img1],[i],None,[256],[0,256])
        histr2 = cv2.calcHist([img2],[i],None,[256],[0,256])
        ValRGB += cv2.compareHist(histr1, histr2, cv2.cv.CV_COMP_CORREL)
    return 3.0 - ValRGB  <= 0.4


def PicDimensions(myPic):
    im = cv2.imread(myPic)
    return im.shape 

def FindPic(mainPic,subPic):
    mHeight,mWidth,mChan = PicDimensions(mainPic)
    sHeight,sWidth,sChan = PicDimensions(subPic)
    if sWidth > mWidth or sHeight >mHeight:
        raise NameError('Illegal images dimensions')
    mIm = cv2.imread(mainPic)
    sIm = cv2.imread(subPic)

    

    print("\n\nI'm looking for your image..........")
    v,s = 0,0
    flag1=False
    for i in range(0,mHeight):
        data = np.zeros( (sHeight,sWidth,3), dtype=np.uint8 )
        if flag1: break
        if sHeight + i > mHeight:
            print("\n\nSorry.. found nothing...")
            break
        for j in range(0,mWidth):

            if sWidth + j > mWidth: break
            
            for k in range(i,i+sHeight):

                for t in range(j,j+sWidth):

                    data[s,v] = mIm[k,t]
                    v+=1
                s+=1
                v=0
            s=0
            if CompereHistograms(sIm,data):
                cv2.rectangle(mIm, (t-sWidth, k-sHeight), (t, k), (255,0,0), 2)
                cv2.imshow('Got it!!',mIm)
                print('\nGot it!!')
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                flag1=True
                break


raised = True
while raised:            
    mainPic = raw_input("Please enter the image you want to work on: ")
    subPic = raw_input("Now enter the image you want to find: ")
    try:
        FindPic(mainPic,subPic)
        raised = False
    except NameError:
        print('\nIllegal images dimensions, try again....\n\n')

    except AttributeError:
        print('\nOne or two of the images are not known, try again....\n\n')




