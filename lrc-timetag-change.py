# 将.lrc歌词全部提前或推迟, 并以原文件名覆盖保存
import os
import re

# 文件名
filename = ''

# 歌词
lrc = ''

def readfile():
	""" 打开(.lrc)文件并返回文件内容 """
	global filename
	filename = input('filename(.lrc):')
	filename = filename.replace('"', '', 2)	# 将两个"删去
	if os.path.isfile(filename):
		if os.path.exists(filename):
			# file exists
			try:
				with open(filename, 'r', encoding='utf-8') as fp:
					return fp.read()
			# 若出现错误, 需要更改为utf-8
			except UnicodeDecodeError:
				print('\a文件编码不支持!')
				os.system('pause')
				return 0
		else:
			# file not exists
			return 0
	else:
		# not a normal file
		return 0

def change(second):
	""" 修改并写回改变后的内容 """
	global lrc
	# 找到时间标签, 匹配 [01:23.456]
	timestamp = re.findall('\[([0-9]{0,3}\:[0-9]{0,2}\.[0-9]{0,3})\]', lrc)
	timestamp_n = []
	for i in range(len(timestamp)):
		min = timestamp[i].split(':')
		second_n = int(min[0]) * 60 + float(min[1]) - second
		if second_n < 0:	# 避免出现负值
			second_n = 0
		min_n = second_n // 60
		second_n = second_n % 60
		timestamp_n.append(('%02d' % min_n) + ':' + ('%05.2f' % second_n))
		lrc = lrc.replace(timestamp[i], timestamp_n[i])
	return lrc

def save():
	""" 覆盖保存文件 """
	with open(filename, 'w', encoding='utf-8') as fp:
		fp.write(lrc)

def main():
	""" 主函数 """
	global lrc

	# 读取文件
	while True:
		lrc = readfile()
		if not lrc:
			print('\aNot Found!  (文件名为文件夹 或 文件不存在)\n')
		else:
			break

	# 询问提前时间
	while True:
		try:
			second = float(input('输入歌词要提前的时间(s): '))
			break
		# 防止输入非数字导致的程序终止
		except ValueError:
			print('请输入数字!\n\a')

	# 修改lrc
	lrc = change(second)

	# 提示保存
	while True:
		result = input('是否覆盖并保存(Y/N)? ')
		if result == 'Y' or result == 'y':
			save()
			break
		if result == 'N' or result == 'n':
			break

if __name__ == "__main__":
	main()
