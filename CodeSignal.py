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

        self.mLucky = self.isLucky(n=1230)

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

    def isLucky(self, n):

        s = str(n)
        lstr = list(s)
        f = lambda x: int(x)
        lint = list(map(f, lstr))
        halfIndex = len(lint) // 2
        firstHalf = lint[0:halfIndex]
        secondHalf = lint[halfIndex:]
        if sum(firstHalf) == sum(secondHalf):
            return True
        else:
            return False


class EdgeOfTheOcean:
    def __init__(self):
        self.mintAdjaisentProd = self.adjacentElementsProduct(inputArray=[-23, 4, -3, 8, -12])
        # self.mintShapeArea=self.shapeArea(n=996) #maximum recursion depth exceeded in comparison
        self.mlStatues = self.makeArrayConsecutive2(statues=[6, 2, 3, 8])
        self.mbAlmostIncreas = self.almostIncreasingSequence(sequence=[1, 2, 5, 3, 5])

    ############################################----adjacentElementsProduct ----#########################################################
    def adjacentElementsProduct(self, inputArray):
        maxProd = -float('inf')
        for i in range(0, len(inputArray) - 1):
            temp = inputArray[i] * inputArray[i + 1]
            if temp > maxProd:
                maxProd = temp

        return maxProd

    ############################################----adjacentElementsProduct ----#########################################################

    def shapeArea(self, n):
        if n == 1:
            return 1
        else:
            return self.shapeArea(n - 1) + 4 * (n - 1)

    # for counter, value in enumerate(a):

    def makeArrayConsecutive2(self, statues):
        statues.sort()
        missingStatues = []
        for i in range(len(statues) - 1):
            if statues[i + 1] - statues[i] > 1:
                dif = statues[i + 1] - statues[i]

                lGaps = list(range(1, dif))
                for j in range(len(lGaps)):
                    temp = statues[i] + lGaps[j]
                    missingStatues.append(temp)
                i += 1

        return missingStatues

    # def almostIncreasingSequence(self, sequence):
    #
    #             return True
    #         for i in range(1,len(sequence)):
    #             if k==0:
    #                 if sequence[i -1] > sequence[i] and i==1:
    #                     sequence.pop(i-1)
    #                     break
    #             if k==1:
    #                 if sequence[i -1] > sequence[i] and i==1:
    #                     sequence.pop(i)
    #                     break
    #
    #
    #
    #             elif sequence[i-1] > sequence[i]:
    #                 sequence.pop(i-1)#remove next
    #                 break
    #
    #         for j in range(1,len(sequence) ):
    #             if sequence[j-1] > sequence[j]:
    #                 trial+=1
    #
    #


class ExploringTheWaters:
    def __init__(self):
        self.mlAlternSum = self.alternatingSums(a=[50, 60, 60, 45, 70])
        self.mSimilar = self.areSimilar(A=[1, 2, 3], B=[2, 1, 3])

    def alternatingSums(self, a):
        first = 0
        last = 0
        for i in range(len(a)):
            if i % 2 == 0:
                first += a[i]
            else:
                last += a[i]
        return [first, last]

    def areSimilar(self, A, B):

        r = []
        for i in range(len(A)):
            if A[i] != B[i]:
                r.append([A[i], B[i]])

        if len(r) == 0 or len(r) == 2 and r[0] == r[1][::-1]:  # reverse list [::-1] It's smart, It reverse [[aaa][bbb]]
            return True
        return False


class IslandOfKnowladge:
    pass


class RainsOfReason:
    pass


class ThroughTheFog:
    pass


class Interviews:
    def __init__(self):
        ############################################----firstNotRepeatingCharacter ----#########################################################
        self.mstrFirstNonRepeating = self.firstNotRepeatingCharacter(s='z')
        self.mintFirstDuplicates = self.firstDuplicate(a=[2, 1, 3, 5, 3, 2])
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

    def firstDuplicate(self, a):
        dic = {}
        for i in a:
            dic[i] = dic.get(i, 0) + 1
            if dic[i] == 2:
                return i
        else:
            return -1


class TestProblems():
    def __init__(self):
        self.mlSimpleSort = self.simpleSort(arr=[2, 4, 1, 5])

    def simpleSort(self, arr):
        n = len(arr)
        for i in range(n):
            j = 0
            stop = n - i
            while j < stop - 1:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
        return arr


explorWaters = ExploringTheWaters()
edge = EdgeOfTheOcean()
smoothSail = SmoothSailing()
intervi = Interviews()
test = TestProblems()
print('end')
