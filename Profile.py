from enum import Enum


class Sex(Enum):
    Woman = 0
    Man = 1


class Profile:
    def __init__(self, sex, FTP=None, weight=None, FTWperKg=None, imgPath=None):
        self.sex = sex
        self.weight = weight if weight > 0 else None
        self.FTP = FTP if FTP > 0 else None
        # 有工体比（MPO）数据 或者 无体重和FTP数据 时，直接套用工体比数据
        self.FTWperKg = FTWperKg if FTWperKg > 0 else FTP / weight
        # 头像路径
        self.imgPath = imgPath
