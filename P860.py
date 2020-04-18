# 860. 柠檬水找零
from typing import List


class P860(object):

    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        Fnum = 0
        Tnum = 0
        for bill in bills:
            if bill == 5:
                Fnum += 1
            elif bill == 10:
                Fnum -= 1
                if Fnum < 0:
                    return False
                Tnum += 1
            else:
                if Tnum == 0:
                    Fnum -= 3
                    if Fnum < 0:
                        return False
                else:
                    Tnum -= 1
                    Fnum -= 1
                    if Fnum < 0:
                        return False
        return True
