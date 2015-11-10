from PIL import Image

import sys

size_iphone4s = 640, 920
size_iphone5s = 640, 1096
size_iphone6 = 750, 1334
size_iphone6s = 1242, 2208
size_ipad = 1536, 2048
size_ipad_pro = 2048, 2732
size_list = [size_iphone4s, size_iphone5s, size_iphone6, size_iphone6s, size_ipad, size_ipad_pro]
#size_list = [size_ipad, size_ipad_pro]

for file_name in sys.argv[1:]:
	print "Processing " + file_name + "..."
	file_prefix = file_name.split(".")[0]
	image = Image.open(file_name)
	for size in size_list:
		new_image = image.resize(size, Image.ANTIALIAS)
		new_file_name =file_prefix + "_" + str(size[0]) + "*" + str(size[1]) + ".jpg"
		new_image.save(new_file_name, "JPEG")
		print 'success save ' + new_file_name
print "Successful All!"
