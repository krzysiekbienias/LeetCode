from typing import List
import numpy as np
from collections import Counter


class stringOperations:
    def __init__(self):
        self.b_abcheck=self.ABCheck(str='Laura sobs')

    def ABCheck(self,str):
        for i in range(len(str)-4):
            if ord(str[i]) == 97 and ord(str[i + 4]) == 98:
                return True
        else:
            return False


strOperations=stringOperations()
print("the end")