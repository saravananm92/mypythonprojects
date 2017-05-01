#!/usr/bin/python


#This script converts the image from input argument to binary form
#Meant to be used to get the binary image for OLED display

import sys
import cv2
import numpy as np
import getopt


def parse_opts(argv):
	inputfile = ''
	try :
		opts,args = getopt.getopt(argv[1:],"hi:s:",["img=","size="])
	except getopt.GetoptError:
		print argv[0]+' -i <input image file> -s <bmp image size in pixels>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h' or opt == '':
			print argv[0]+' -i <input image file> -s <bmp image size in pixels>'
			sys.exit()
		elif opt in ("-i","--img"):
			inputfile = arg
		elif opt in ("-s","--size"):
			size = int(arg)
			if (size % 8):
				print "Size must be divisible by zero : ",size
				sys.exit()
	print "Input image : ",inputfile
	print "size of bmp image needed :",size
	return (inputfile,size)
  
def process_img(image,size):
	im = cv2.imread(image)
	im2 = cv2.resize(im,(size,size))
	im3 = cv2.cvtColor(im2,cv2.COLOR_RGB2GRAY)
	ret,bin_im = cv2.threshold(im3,150,255,cv2.THRESH_BINARY_INV)
	cv2.imshow("binary image",bin_im)
	cv2.waitKey()
	for row in range(size):
		row_val = ""
		for col in range(size/8):
			row_val = row_val + "B"
			for i in range(8):
				row_val = row_val + str(bin_im[row][col*8+i]/255)
			row_val = row_val + ","
		print row_val
	


if __name__ == "__main__":
	inputfile,size = parse_opts(sys.argv)
	process_img(inputfile,size)
