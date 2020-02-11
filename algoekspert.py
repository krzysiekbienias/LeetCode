from typing import List


class Arrays:
    def __init__(self):

        self.mli_two_sum = self.two_number_sum(array=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
        self.mThreeSum = self.three_number_sum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], target=0)

    ########################################----Two Sum ----######################################################
    # O(nlog(n))|O(1)
    def two_number_sum(self, array: List[int], target: int) -> List[int]:
        array.sort()
        l_pointer = 0
        r_pointer = len(array) - 1
        while l_pointer < r_pointer:
            current_sum = array[l_pointer] + array[r_pointer]
            if current_sum == target:
                return [array[l_pointer], array[r_pointer]]
            elif current_sum < target:
                l_pointer += 1
            elif current_sum > target:
                r_pointer -= 1
        return []

    ########################################----Two Sum ----######################################################

    ########################################----Three Sum ----######################################################
    def removeDuplicatesHelper(self, nums: List[int]) -> int:
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                del nums[i]
            else:
                i+=1
        return nums


    # O(n^2)|O(n)#time limit exceeded 312 / 313 test cases passed.
    def three_number_sum(self, array, target):
        array.sort()
        triplets = []
        for i in range(len(array) - 2):  # last two numbers  will be left and right pointer
            leftPointer = i + 1
            rightPointer = len(array) - 1
            while leftPointer < rightPointer:  # do until pointers don't overlap each other
                currentSum = array[i] + array[leftPointer] + array[rightPointer]
                if currentSum == target:
                    triplets.append([array[i], array[leftPointer], array[rightPointer]])
                    leftPointer += 1
                    rightPointer -= 1
                elif currentSum < target:
                    leftPointer += 1
                elif currentSum > target:
                    rightPointer -= 1
        triplets.sort()
        tripletsWithoutDuplicates=self.removeDuplicatesHelper(nums=triplets)


        return tripletsWithoutDuplicates

    def smallestDifference(self,arrayOne,arrayTwo):
        arrayOne.sort()
        arrayTwo.sort()
        idxOne=0
        idxTwo=0
        smallest=float("inf")
        current=float("inf")
        smallesPair=[]
        while idxOne<len(arrayOne) and idxTwo<len(arrayTwo):
            firstNum=arrayOne[idxOne]
            secondNum=arrayTwo[idxTwo]
            if firstNum<secondNum:
                current=secondNum-firstNum
                idxOne+=1
            elif secondNum<firstNum:
                current=firstNum-secondNum
                idxTwo+=1
            else: #firstNum-secondNum=0
                return [firstNum,secondNum]
            if smallest>current:
                smallest=current
                smallesPair=[firstNum,secondNum]
        return smallesPair

    def moveElementToEnd(self,array,toMove):
        i=0
        j=len(array)-1
        while i <j:
            while i<j and array[j]==toMove:
                j-=1
            if array[i]==toMove:
                array[i],array[j]=array[j],array[i]
            i+=1
        return array

########################################----Three Sum ----######################################################


class Sorting:
    def __init__(self):
        self.ml_booble = self.booble_sort(array=[4, 2, 3, 5, 1, 5, 4])

    def booble_sort(self, array):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    self.swap(i, i + 1, array)
                    is_sorted = False
        return array

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]


class Recursion:
    def __init__(self):
        self.m_pow_set = self.powerset(array=[1, 2, 3])

    def powerset(self, array, idx=None):  # recursive
        if idx is None:
            idx = len(array) - 1
        elif idx < 0:
            return [[]]
        ele = array[idx]
        subsets = self.powerset(array, idx - 1)
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [ele])
        return subsets


class Strings:
    def __init__(self):
        self.cipher=self.cipherEncryptor()

    ########################################----Cesar Cipher Encryptor ----#############################################

    def shift_letter(self, letter, move):
        newLetterCode = ord(letter + move)
        if newLetterCode <= 122:
            return chr(newLetterCode)
        else:
            return chr(97 + newLetterCode % 122)

    def cipherEncryptor(self, string, move):
        encryptedPassword = []
        wrappedMove = move % 26
        for letter in string:
            encryptedPassword.append(self.shift_letter(letter=letter, move=wrappedMove))
        return "".join(encryptedPassword)

    ########################################----Cesar Cipher Encryptor ----#############################################

class Searching:
    def __init__(self):
        self.l_findThreeLargestNumbers=self.findThreeLargestNumbersMySol(array=[141,1,17,-7,-17,-27,18,541,8,7,7])

    ########################################---- Find Three Largest Numbers ----#############################################
    #if we can sort array
    #O(nlog(n))
    def findThreeLargestNumbersMySol(self, array):
        array.sort()
        return array[-3:]

    #we can do better O(n)
    def findThreeLargestNumbers(self,array):
        threeLargest=[None,None,None]
        for num in array:
            self.updateLargest(threeLargest,num)
        return threeLargest

    def updateLargest(self,threeLargest,num):
        if threeLargest[2] is None or num>threeLargest[2]:
            self.shiftAndUpdate(threeLargest,num,2)
        elif threeLargest[1] is None or num>threeLargest[1]:
            self.shiftAndUpdate(threeLargest,num,1)
        elif threeLargest[0] is None or num>threeLargest[0]:
            self.shiftAndUpdate(threeLargest,num,0)

    def shiftAndUpdate(self,array,num,idx):
        for i in range(idx+1)
            if i==idx:
                array[i]=num
            else:
                array[i]=array[i+1]
    ########################################----Find Three Largest Numbers ----#############################################








arrays_algo = Arrays()
sorting_algo = Sorting()
recursion_algo = Recursion()
searching_algo=Searching()

print('the end')
