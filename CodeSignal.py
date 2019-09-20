from typing import List
import numpy as np
from collections import Counter


class SmoothSailing:
    def __init__(self):
        ############################################----sortByHeight ----#########################################################
        self.mliSorted = self.sortByHeight(a=[-1, 150, 190, 170, -1, -1, 160, 180])
        ############################################----sortByHeight ----#########################################################

        ############################################----commonCharacterCount ----#########################################################
        self.mintCommon = self.commonCharacterCount(s1='abca', s2='xyzbac')
        ############################################----commonCharacterCount ----#########################################################

        ##############################################

    def sortByHeight(self, a: List[int]) -> List[int]:  # Andrew_Pudge solution
        l = sorted([i for i in a if i > 0])
        for counter, value in enumerate(a):
            if value == -1:
                l.insert(counter, value)
        return l

    def commonCharacterCount(self, s1, s2):
        dic1 = {}
        dic2 = {}
        for ch in s1:
            dic1[ch] = dic1.get(ch, 0) + 1
        for ch in s2:
            dic2[ch] = dic2.get(ch, 0) + 1
        lk1 = list(dic1.items())
        lk2 = list(dic2.items())
        counter = 0

        for i in range(len(lk1)):
            for j in range(len(lk2)):
                if lk1[i][0] == lk2[j][0]:
                    temp = min(lk1[i][1], lk2[j][1])
                    counter += temp
        return counter

class EdgeOfTheOcean:




class Interviews():
    def __init__(self):
        ############################################----firstNotRepeatingCharacter ----#########################################################
        self.mstrFirstNonRepeating = self.firstNotRepeatingCharacter(s='z')
        self.mintFirstDuplicates=self.firstDuplicate(a=[2, 1, 3, 5, 3, 2])
        ############################################----firstNotRepeatingCharacter ----#########################################################

    def firstNotRepeatingCharacter(self, s: str) -> str:
            if s == "":
                return -1
            elif len(s) == 1:
                return s
            dic = {}
            for ch in s:
                dic[ch] = dic.get(ch, 0) + 1
                l_chfrequency = list(dic.values())
            if 1 not in l_chfrequency:
                return '_'
            for ch in s:
                if dic[ch] == 1:
                    return ch

    def firstDuplicate(self,a):
        dic = {}
        for i in a:
            dic[i] = dic.get(i, 0) + 1
            if dic[i]==2:
                return i
        else:
            return -1




edge = EdgeOfTheOcean()
smoothSail=SmoothSailing()
intervi=Interviews()




print('end')