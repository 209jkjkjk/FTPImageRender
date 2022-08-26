from Tool import *


if __name__ == '__main__':
    # 读取FTP图片以及社友的数据
    DATA = loadData()
    FTPImage = makeImg(DATA)
    FTPImage.show()
