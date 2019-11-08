import cv2
import os
import numpy as np
from PIL import Image,ImageFilter


path = './annotations/'

for filename in os.listdir(path):
    filen=filename.split(".", 1)
    if (len(filen)>1):
	    print(filen[1])

	    if (filen[1]=="jpg"):

		    img = cv2.imread(path+filename, cv2.IMREAD_UNCHANGED)

		    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		    cv2.imwrite('./annotations/gray/'+'_gray'+filename+'.jpg',gray )
   
print('OH YEAHHHH!!')
