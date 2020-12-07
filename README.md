# python_doc_scanner
This app made for linux. It can work on windows if required dependencies are installed.


With this app you can scan your papers and convert them into .pdf file format.

Dependencies:
- imagemagick
- poppler-utils
- Python opencv package

Installing Dependencies:

Imagemagick
$ sudo apt install imagemagick

poppler-utils
$ sudo apt install poppler-utils

Python opencv package

If you're using a python virtual environment:

(env) $ pip install opencv-python

Not using python virtual environment:

$ pip3 install opencv-python

After that run del_images.py in order to delete the images in the directories:

(env) $ python del_images.py
or
$ python3 del_images.py


Now copy your images to Images directory. If you don't find any images and want to try the app. There are 2 images in the Images_1 directory copy them and paste them into Images directory

Run main.py:
(env) $ python main.py
or
$ python3 main.py

Now you can see the cropped images in Scanned_images directory. Also the pdf will appear in the current directory which you run the main.py

To make your images white and black only. In other words, If you would like to perform thereshold to your images, Run th_images.py

(env) $ python th_image.py
or
$ python3 th_image.py

After that there will be a pdf in the current directory and the thresholded images will be in TH_Images directory.

You can reduce your pdf size from online pdf compressor sites.

