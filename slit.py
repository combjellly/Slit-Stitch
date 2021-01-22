import sys
from PIL import Image
import glob
import os
import fnmatch

#### PD PATCH OR CUSTOM PATH
try:

	location=open("location.txt","r+")
	location = location.read().replace(";","").replace("\n","")
	option = 1
	savepath = location.split("/")
	del savepath[-1]
	savepath = "/".join(savepath)
	print(location)

except:
	pass

if option != 1:
	print("using default settings")
	location=input("where did you put images saved from PD?[.tif]")
	location= location.replace(" ","/")
	option = 2


def go(location,option,savepath):

	# Open a file
	path = location
	imgformat = "*.tif"

	if option == 2:
		dirs = os.listdir(path)

		#This would print all the files and directories
		for file in os.listdir(path):
			if fnmatch.fnmatch(file, '*.tif'):
				print (file)
	else:
		pass

	image_list = []
	for filename in glob.glob(path+imgformat): 
	    im=Image.open(filename)
	    image_list.append(im)

	######
	list_im = [image_list]

	images = image_list
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in images:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	new_im.save(savepath+'/slittest.png')
	print("done :-)")

go(location,option,savepath)