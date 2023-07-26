class Batman:
    def __init__(self, hp):
        self.hp = hp

    @property
    def hp(self):#method名必需一樣
        return self._hp #將hp存成_hp並回傳

    @hp.setter
    def hp(self, hp):#method名必需一樣
        if hp > 100:
            self._hp = 100

        elif hp < 0:
            self._hp = 0

        else:
            self._hp = hp

b1 = Batman(150)
print(b1.hp)

#decorter 式分別去裝飾而不是由上到下去執行

