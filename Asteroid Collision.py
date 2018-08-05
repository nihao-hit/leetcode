class Solution:
    def asteroidCollision(self,asteroids):
        '''
        :type asteroids:List[int]
        :rtype:List[int]
        '''
        out = []
        for i in asteroids:
            if out:
                if i > 0:
                    out.append(i)
                else:
                    if out[-1] < 0:
                        out.append(i)
                    else:
                        if out[-1] == abs(i):
                            out.pop()
                        elif out[-1] < abs(i):
                            out[-1] = i
                            collision = True
                            while len(out)>=2 and collision:
                                if out[-2] > 0:
                                    if out[-2] > abs(out[-1]):
                                        out.pop()
                                        collision = False
                                    elif out[-2] == abs(out[-1]):
                                        out.pop()
                                        out.pop()
                                        collision = False
                                    else:
                                        out[-2] = out[-1]
                                        out.pop()
                                else:
                                    collision = False
            else:
                out.append(i)
        return out
'''
难点在于21行：如何迭代来解决方向为左的i与out中元素产生的碰撞？
栈
'''