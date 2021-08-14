import os
import hashlib

MD5_dict = {}
file_num = 0

def lsMD5(lin):
    ''' 遍历文件计算MD5,存入MD5_dict '''
    global file_num
    error_Permission = '\tError: PermissionError!\t可能产生的原因是文件找不到, 或者被占用, 或者无权限访问.'
    error_FileNotFound = '\tError: FileNotFoundError!\t 找不到指定路径.'
    error_NotADirectory = '\tError: NotADirectoryError!\t不是文件夹.'
    try:
        # 获取路径下的文件(夹)列表
        ls = os.listdir(lin)
    except PermissionError:
        print(error_Permission)
    except FileNotFoundError:
        input(error_FileNotFound)
        exit()
    except NotADirectoryError:
        input(error_NotADirectory)
        exit()
    else:
        for name in ls:
            link = lin + name
            if os.path.isfile(link):
                # 为文件
                file_num += 1
                try:
                    with open(link, 'rb') as fp:
                        # 取MD5.转十六进制.转大写
                        MD5 = hashlib.md5(fp.read()).hexdigest().upper()
                        if MD5 not in MD5_dict:
                            MD5_dict[MD5] = [link]
                        else:
                            MD5_dict[MD5].append(link)
                            # print('MD5: ' + MD5)
                except PermissionError:
                    print(error_Permission)
            elif os.path.isdir(link):
                # 为文件夹,递归查找
                lsMD5(link + '/')

def main(link):
    print('find...')
    # 更正传入路径格式
    if link == '':
        link = './'
    link = link.replace('"', '').replace('\\', '/')
    if link[-1] != '/':
        link += '/'

    # 计算MD5
    lsMD5(link)
    print(f'包含文件数: {file_num}')

    repeat = []
    for r in MD5_dict.values():
        # 找到相同的文件,存入repeat列表
        if len(r) > 1:
            repeat.append(r)

    if len(repeat):
        print('重复文件组: ' + str(len(repeat)))
        with open('./repeat.csv', 'w', encoding='utf_8_sig') as fp:
            for line in repeat:
                for each_file in line:
                    fp.write(str(each_file) + ',')
                # print(line)
                fp.write('\n')
    else:
        input('没有重复文件')

if __name__ == "__main__":
    main(input('输入文件夹路径: '))
