import cv2
import os

images = os.listdir('./Scanned_images/')
images.sort()

c = 12
a = 125
image_counter = 0
for image in images:
    image_counter += 1

os. system('rm -f ./TH_Images/*')
for image in images:
    img = cv2.imread('./Scanned_images/'+image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,a,c)
    cv2.imwrite('./TH_Images/'+image,th2)

convert_line = 'convert '
counter = 0
for image in images:
    if counter == 35:
        break
    convert_line += "'./TH_Images/" + image + "' "
    counter += 1

convert_line += 'TH_images.pdf'

os.system(convert_line)
convert_line = 'convert '
counter = 0
if image_counter > 35:
    for image in images:
        counter += 1
        if counter > 35:
            convert_line += "'./TH_Images/" + image + "' "

    convert_line += 'TH_images2.pdf'
    os.system(convert_line)
    merge_line = 'pdfunite TH_images.pdf TH_images2.pdf TH_images_merged.pdf'
    os.system(merge_line)
    os.system('rm -f TH_images.pdf TH_images2.pdf')
