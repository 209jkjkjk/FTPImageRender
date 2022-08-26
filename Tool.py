import numpy as np
from Profile import *
from PIL import Image


class Data():
    # 头像大小
    AVATAR_SIZE = 24
    # 添加头像的边界
    X_MAN_OFFSET = 519 - AVATAR_SIZE
    X_MAN_LIMIT = 0
    X_WOMAN_OFFSET = 977 - AVATAR_SIZE
    X_WOMAN_LIMIT = 595
    # 基础定位偏移
    Y_OFFSET = 162


def loadData():
    data = Data()
    # 读取FTP级别数据
    configFile = np.loadtxt("FTPLever.data", delimiter="\t", dtype=float)
    # 转置提取列
    configFile = configFile.T
    # 截取FTP数据
    data.ManFTWperKg = configFile[3]
    data.WomanFTWperKg = configFile[7]

    # 读取社友的数据
    data.athletes = []
    with open("profiles.data", encoding="UTF-8") as profileFile:
        # 去掉表头
        print("读取数据：\n" + profileFile.readline(), end="")
        while True:
            # 读取每一行 但没有换行符
            line = profileFile.readline().strip("\n")
            if not line: break

            # 尝试处理每一行数据（姓名 性别 FTP 体重 工体比 头像）
            try:
                args = line.split("\t")
                print(args)
                # 快速检测
                if len(args) < 6:
                    raise Exception()

                sex = None
                if args[1] == "male":
                    sex = Sex.Man
                if args[1] == "female":
                    sex = Sex.Woman
                FTP = float(args[2])
                weight = float(args[3])
                WperKG = float(args[4])
                # 添加数据到字典
                data.athletes.append(Profile(sex, FTP, weight, WperKG, args[5]))

                # 计算位置（向下取整，谦虚一点）
                athlete = data.athletes[-1]
                if athlete.sex == Sex.Man:
                    athlete.rank = np.sum(data.ManFTWperKg >= athlete.FTWperKg) - 1
                if athlete.sex == Sex.Woman:
                    athlete.rank = np.sum(data.WomanFTWperKg >= athlete.FTWperKg) - 1
            except Exception:
                print("↑行内数据错误，已跳过↑")

    return data


def getPosition(athlete, lastPosition):
    # 头像添加位置的偏移量和限制
    if athlete.sex == Sex.Man:
        Xoffset, Xlimit = Data.X_MAN_OFFSET, Data.X_MAN_LIMIT
    elif athlete.sex == Sex.Woman:
        Xoffset, Xlimit = Data.X_WOMAN_OFFSET, Data.X_WOMAN_LIMIT
    else:
        raise Exception("未知性别")

    # 假定位置
    Y = Data.Y_OFFSET + int(athlete.rank * 23.5)
    X = Xoffset
    # 修正位置
    if lastPosition and Y == lastPosition[1] and X >= lastPosition[0]:
        X = lastPosition[0] - Data.AVATAR_SIZE
    # 验证位置
    if X < Xlimit:
        raise Exception("人太多了，一行挤不下，赶紧更新程序")
    return X, Y


def makeImg(data):
    # 按照位置排序
    data.athletes.sort(key=lambda x: x.rank)
    # 读取背景图
    FTPImage = Image.open("FTP.jpg")
    # 记录上次图片位置
    lastposition = None
    for athlete in data.athletes:
        lastposition = position = getPosition(athlete, lastposition)
        FTPImage.paste(Image.open(athlete.imgPath).resize((Data.AVATAR_SIZE, Data.AVATAR_SIZE)), position)
    return FTPImage
