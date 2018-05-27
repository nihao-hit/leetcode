class Solution():
    def intToRoman(self,num):
        '''
        :param num:int
        :return: str
        '''
        Roman = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        romans = []
        global x, y
        x = y = num
        def intToRoman(x,c):
            if x == 9:
                romans.extend(Roman[c/10]+Roman[c])
            elif x == 4:
                romans.extend(Roman[c/10]+Roman[c/2])
            else:
                x1, y1 = divmod(x, 5)
                romans.extend(x1 * Roman[c/2] + y1 * Roman[c/10])
        while True:
            if y >= 1000:
                x,y = divmod(x,1000)
                romans.extend(x*'M')
            elif y >= 100:
                x,y = divmod(y,100)
                intToRoman(x,1000)
            elif y >= 10:
                x,y = divmod(y,10)
                intToRoman(x, 100)
            else:
                intToRoman(y, 10)
                break
        return ''.join(romans)