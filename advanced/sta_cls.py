class Batman:
    def __init__(self, hp):
        self.hp = hp

    
    def f(self):
        print('Test classmethod')

    @staticmethod #使用與class無關的函式時，會使用到
    def count_num():
        print(1 + 2)


    @classmethod #需使用class中有self的函式功能時，會使用到
    def test(cls):
        cls(100).f() #暫時創作實例
        #當class有參數時，cls()括號中也需放參數

Batman.test()
Batman.count_num()
