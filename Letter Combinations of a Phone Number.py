from functools import reduce
class Solution:
    def letterCombinations(self,digits):
        '''

        :param digits:str
        :return: List[str]
        '''
        if not digits:
            return []
        letter = {'2':'abc','3':'def',
                  '4':'ghi','5':'jkl',
                  '6':'mno','7':'pqrs',
                  '8':'tuv','9':'wxyz'}
        return reduce(lambda init,y: [i+j for i in init
                                    for j in letter[y]],digits,[''])