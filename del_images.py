import os

del_scanned_images = 'rm -f ./Scanned_images/*'
del_img = 'rm -f ./Images/*'
del_th_images = 'rm -f ./TH_Images/*'

os.system(del_scanned_images)
os.system(del_img)
os.system(del_th_images)
