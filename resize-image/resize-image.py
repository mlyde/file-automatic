import cv2
import os
import numpy as np

# cut 裁剪后的 xy
target_x = 286
target_y = 203

def get_dir(dir):
	""" 遍历文件夹下所有的文件名 """

	list1 = os.listdir(dir)
	for l in list1:
		l = f'{dir}/{l}'
		if(os.path.isdir(l)):
			get_dir(l)
		else:
			cut(l)
			# cut2(l,x=800)
			# cut2(l,y=400)

def cut(inputdir = './t.jpg'):
	""" 图片裁剪 """

	# 裁剪后的文件名为
	# outputdir = inputdir[:-4] + '_over.jpg'
	# 设置为相同文件名,覆盖原文件
	outputdir = inputdir

	# img = cv2.imread(inputdir)	# imread读取不能包含中文文件名
	img = cv2.imdecode(np.fromfile(inputdir, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

    # imdecode读取图像默BGR通道排列, 
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)	# 转换为RGB

	# img.shape:[height,width,channel]
	in_y, in_x = img.shape[:2]
	print(img.shape)

	scale = target_x / target_y
	scale1 = in_x / in_y

	if(scale1 >= scale):
		size = (int(in_x/(in_y/target_y)), target_y)
		# print(1, size)
	elif(scale1 < scale):
		size = (target_x, int(in_y/(in_x/target_x)))
		# print(2, size)
	else:
		size = (target_x, target_y)
		print('error')

	# 缩放到size=(x,y)
	resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

	# 展示裁剪后的图片
	# cv2.imshow('image', resized)
	# cv2.waitKey(0)
	# print('x', resized.shape[1], 'y', resized.shape[0])

	if(resized.shape[1] == target_x):
		# x=target_x
		y0 = resized.shape[0] // 2 - target_y//2
		y1 = y0 + target_y
		x0 = 0
		x1 = target_x
	if(resized.shape[0] == target_y):
		# y=target_y
		y0 = 0
		y1 = target_y
		x0 = resized.shape[1] // 2 - target_x//2
		x1 = x0 + target_x

	output_img = resized[y0:y1, x0:x1]

	# cv2.imwrite(outputdir, output_img)	# imwrite保存文件名不能包含中文
	cv2.imencode('.jpg', output_img)[1].tofile(outputdir)

def cut2(inputdir = './t.jpg', x=0, y=0):
	""" 等比缩放,不裁剪 """
	# outputdir = inputdir[:-4] + '_over.jpg'
	outputdir = inputdir
	img = cv2.imdecode(np.fromfile(inputdir, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

	in_y, in_x = img.shape[:2]
	if(x):
		# 等比缩小为x=
		fxy = x/in_x
	elif(y):
		# 等比缩小为y=
		fxy = y/in_y
	else:
		fxy = 1

	# 按比例缩放,fx:x轴缩放比例,fy:y轴缩放比例
	output_img = cv2.resize(img, (0,0), fx=fxy, fy=fxy, interpolation=cv2.INTER_AREA)
	cv2.imencode('.jpg', output_img)[1].tofile(outputdir)

if __name__ == "__main__":
	original_dir = input('文件夹路径:')
	get_dir(original_dir)
