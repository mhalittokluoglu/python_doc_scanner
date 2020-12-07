import os
import cv2
import utilities


images = os.listdir('./Images/')



images.sort()
image_counter = 0
for image in images:
    image_counter += 1

os.system('rm -f ./Scanned_images/*')
for image in images:
    img = utilities.scan_image('./Images/'+image)
    cv2.imwrite('./Scanned_images/'+image,img)

convert_line = 'convert '

counter = 0
for image in images:
    if counter == 35:
        break
    convert_line += './Scanned_images/'+image+' '
    counter = counter + 1

convert_line += 'Scanned_images.pdf'

os.system(convert_line)

if image_counter >= 35:
    convert_line = 'convert '
    counter = 0
    for image in images:
        if counter >= 35:
            convert_line += './Scanned_images/'+image+' '
        counter = counter + 1
    convert_line += 'Scanned_images2.pdf'
    os.system(convert_line)
    merge_line = 'pdfunite Scanned_images.pdf Scanned_images2.pdf Scanned_images_merged.pdf'
    os.system(merge_line)
    os.system('rm -f Scanned_images.pdf Scanned_images2.pdf')
