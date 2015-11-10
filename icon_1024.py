from PIL import Image

import sys

#size_list = ["28_1", "29_1", "29_2", "29_3",
#		"40_1", "40_2", "40_3", "57_1", "57_2", "60_2", "60_3",
#		"50_1", "50_2", "72_1", "72_2", "76_1", "76_2", "108_1"]
size_list = ["1024_1"]

for file_name in sys.argv[1:]:
	print "Processing " + file_name + "..."
	file_prefix = file_name.split(".")[0]
	image = Image.open(file_name)
	for size_item in size_list:
		size_num = int(size_item.split('_')[0]) * int(size_item.split('_')[1])
		size = size_num, size_num
		new_image = image.resize(size, Image.ANTIALIAS)
		new_file_name =file_prefix + "_" + str(size_item.split('_')[0]) + "_" + str(size_item.split('_')[1]) + "x.png"
		new_image.save(new_file_name, "JPEG")
		print 'success save ' + new_file_name
print "Successful All!"
