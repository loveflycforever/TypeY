import time


class UpoItem:
    def __init__(self, mid, name, sex, face, regtime, birthday, sign, level):
        self.bilibiliId = mid
        self.name = name
        self.sex = sex
        self.avatar = face
        self.registerTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(regtime))
        self.birthday = birthday
        self.sign = sign
        self.level = level
