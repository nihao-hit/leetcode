class Interval:
    def __init__(self,s=0,e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self,intervals):
        '''
        :type intervals:List[Intervals]
        :rtype:List[Interval]
        '''
        out = []
        for interval in sorted(intervals,key=lambda i:i.start):
            if out and out[-1].end >= interval.start:
                out[-1].end = max(out[-1].end,interval.end)
            else:
                out.append(interval)
        return out