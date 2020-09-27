from typing import List


class Arrays:
    def __init__(self):

        self.mli_two_sum = self.two_number_sum(array=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
        self.mThreeSum = self.three_number_sum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], target=0)
        self.b_isMonotonic=self.isMonotonic(array=[1,1,1,2,6,3,5])
        self.l_langestRange=self.largestRange(arr=[1,11,3,0,15,5,2,4,10,7,12,6])
        self.b_subsequecne=self.isValidatedSubsequence(arr=[5,1,22,25,6,-1,8,10],sequence=[1,6,8])




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

    ########################################----Three Sum ----######################################################

    ########################################----Smallest Difference----######################################################
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

    ########################################----Smallest Difference----######################################################

    ########################################----Move elemet to the end----######################################################
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

########################################----Move elemet to the end ----######################################################

########################################---- Is Monotoonic ----######################################################
    def breakDirection(self, direction, prevInt,currentInt):
        #respecting or following direction
        difference=currentInt-prevInt
        if direction>0:
            return difference<0
        return difference>0


    def isMonotonic(self,array):
        if len(array)<=2:
            return True

        direction=array[1]-array[0]
        for i in range(2,len(array)):
            if direction==0:
                direction = array[i] - array[i-1]
                continue
        #we need to define a funtion that checks whether we don't break direction
            if self.breakDirection(direction,array[i-1],array[i]):
                return False
        return True

####second solution
    ########################################----Is Monotoonic----######################################################


    ########################################----Largest Range----######################################################
    def largestRange(self,arr):
        di={}
        longestLenght=0
        bestRange=[]
        for num in arr:
            di[num]=True #label all numbers as true
        for num in arr:
            if not di[num]:#if di[num]==False in my opinion it is equivalent
                continue
            di[num]=False
            currentLength=1
            left =num-1
            right=num+1
            while left in di:
                di[left]=False
                currentLength+=1
                left-=1
            while right in di:
                di[num]=False
                currentLength+=1
                right+=1
            if currentLength>longestLenght:
                longestLenght=currentLength
                bestRange=[left+1,right-1]
        return bestRange
    ########################################----Largest Range----######################################################

    ########################################----Validate Subsequence----######################################################
    def isValidatedSubsequence(self,arr,sequence):
        arrIdx=0
        seqIdx=0
        while arrIdx<len(arr) and seqIdx<len(sequence):
            if arr[arrIdx]==sequence[seqIdx]:
                seqIdx+=1
            arrIdx+=1
        return seqIdx==len(sequence)
    ########################################----Validate Subsequence----######################################################

    ########################################----Validate Subsequence----######################################################
    def smallestDifference(self,arrOne,arrTwo):
        arrOne.sort()
        arrTwo.sort()
        idxOne=0
        idxTwo=0
        smallest=float('inf')
        current=float('inf')
        smallestPair=[]
        while idxOne<len(arrOne) and idxTwo<len(arrTwo):
            firstNum=arrOne[idxOne]
            secondNum=arrTwo[idxTwo]
            if firstNum<secondNum:
                current=secondNum-firstNum
                idxOne+=1
            elif secondNum<firstNum:
                current=firstNum-secondNum
            else:
                return [firstNum,secondNum]
            if smallest>current:
                smallest=current
                smallestPair=[firstNum,secondNum]
        return smallestPair

    ########################################----Validate Subsequence----######################################################







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
        self.s_longestPalindromicSub=self.longestPalindromicSubstring(string='abaxyzzyxf')

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

    ########################################---- Longest Palindromic Substring ----#############################################
    def longestPalindromicSubstring(self,string):
        currentLongest=[0,1]
        for i in range(1,len(string)):
            odd=self.getLongestPalindromeFrom(string,i-1,i+1)
            even=self.getLongestPalindromeFrom(string,i-1,i)
            longest=max(odd,even,key=lambda x:x[1]-x[0])
            currentLongest=max(longest,currentLongest,key=lambda x: x[1]-x[0])
        return string[currentLongest[0]:currentLongest[1]]
     #helper function
    def getLongestPalindromeFrom(self,string,leftIdx,rightIdx):
        while leftIdx>=0 and rightIdx<len(string):
            if string[leftIdx]!=string[rightIdx]:
                break
            leftIdx-=1
            rightIdx+=1
        return [leftIdx+1,rightIdx]
    ########################################----Longest Palindromic Substring ----#############################################

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
        for i in range(idx+1):
            if i==idx:
                array[i]=num
            else:
                array[i]=array[i+1]
    ########################################----Find Three Largest Numbers ----#############################################

    ########################################----Search in Sorted Matrix ----#############################################
    def searchInSortedMatrix(self,matrix,target):
        row=matrix[0][0]
        col=len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col]>target:
                col-=1
            elif matrix[row][col]<target:
                row+=1
            else:
                return [row,col]
        return [-1,-1]
    ########################################----Search in Sorted Matrix ----#############################################


class DynamicProgramming:
    def __init__(self):
        self.i_waterArea=self.waterArea(pillars=[0,8,0,0,5,0,0,10,0,0,1,1,0,3])
        self.i_coinChange=self.coinChange(denoms=[1,2,5],amount=11)
        self.i_maxSubsetSumNoAdjacent=self.maxSubsetSumNoAdjacent(array=[7,10,12,7,9,14])
        #self.li_maxSumIncreasing=self.maxSumIncreasingSubsequence(array=[10,70,20,30,50,11,30])


    def maxSumIncreasingSubsequence(self,array):
        sequences=[None for x in array]
        sums=[num for num in array]
        maxSumIdx=0
        for i in range(len(array)):
            currentNum=array[i]
            for j in range(0,i):
                otherNum=array[j]
                if otherNum<currentNum and sums[j]+currentNum>=sums[i]:
                    sums[i]=sums[j]+currentNum
                    sequences[i]=j
            if sums[i]>=sums[maxSumIdx]:
                maxSumIdx=i
        return [sums[maxSumIdx],self.buildSequence(self,array,sequences,maxSumIdx)]

    def buildSequence(self,array,sequences,currentIdx):
        sequence=[]
        while currentIdx is not None:
            sequence.append(array[currentIdx])
            currentIdx=sequences[currentIdx]
        return list(reversed(sequence))



    ########################################---- Water Area ----#############################################
    #O(n) time,O(n) space
    def waterArea(self,pillars):
        l_watterUnits=[0]*len(pillars)
        l_leftMax=[] #tallest pillar on left of current index
        l_rightMax=[]
        leftMax_i=0
        righMax_i=0
        l_leftMax=l_leftMax+[0]
        for i in range(1,len(pillars)):

            pillar=pillars[i]
            leftMax_i=max(leftMax_i,pillars[i-1])
            l_leftMax.append(leftMax_i)
        #l_rightMax = l_rightMax + [0]
        for i in reversed(range(1,len(pillars))):
            pillar=pillars[i]
            righMax_i=max(righMax_i,pillars[i])
            l_rightMax.append(righMax_i)
        l_rightMax.reverse()
        l_rightMax=l_rightMax+[0]

        # for i in range(len(pillars)):
        #     minHight=l_leftMax[i]


        return None

    ########################################---- Water Area ----#############################################

    ########################################---- Water Area Better space comp----#############################################
    #O(n) time, O(1) space
    def waterAreaImproved(self,pillars):
        if len(pillars)==0:
            return 0
        leftIdx=0
        rightIdx=len(pillars-1)
        leftMax=pillars[leftIdx]
        rightMax=right[rightIdx]
        surface=0
        while leftIdx<rightIdx:
            if(pillars[leftIdx]<pillars[rightIdx]):
                leftIdx+=1
                leftMax=max(leftMax,pillars[leftIdx])
                surface+=leftMax-pillars[leftIdx]
            else:
                rightIdx-=1
                rightMax=max(rightMax,pillars[rightIdx])
                surface+=rightMax-pillars[rightIdx]
        return surface

    ########################################---- Water Area Better space comp----#############################################

    ########################################---- Min numbers of Coins For Change ----#############################################

    def coinChange(self, denoms: List[int], amount: int) -> int:
        l_numOfCoins = [float('inf')] * (amount + 1)
        l_numOfCoins[0] = 0
        for denom in denoms:
            for amount in range(len(l_numOfCoins)):

                if denom <= amount:
                    l_numOfCoins[amount] = min(l_numOfCoins[amount], 1 + l_numOfCoins[amount - denom])
        if l_numOfCoins[amount] == float('inf'):
            return -1
        else:
            return l_numOfCoins[amount]

    ########################################---- Min numbers of Coins For Change ----#############################################

    ########################################---- Maximum subset sum with no adjacent element ----#############################################
    def maxSubsetSumNoAdjacent(self,array):
        if not len(array):
            return 0
        elif len(array)==1:
            return array[0]
        elif len(array)==2:

           return max(array[0],array[1])
        maxSum = [0] * len(array)
        for i in range(2,len(array)):
            maxSum[i]=max(maxSum[i-1],maxSum[i-2]+array[i])
        return maxSum[-1]


#####################Graphs
class Node:
    def __init__(self,name):
        self.children=[]
        self._name=name

    def addChild(self,name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self,array):
        array.append(self._name)
        for child in self.children:
            child.depthFirstSearch(array)
            return array





graph={
  "nodes": [
    {"children": ["B", "C", "D"], "id": "A", "value": "A"},
    {"children": ["E", "F"], "id": "B", "value": "B"},
    {"children": [], "id": "C", "value": "C"},
    {"children": ["G", "H"], "id": "D", "value": "D"},
    {"children": [], "id": "E", "value": "E"},
    {"children": ["I", "J"], "id": "F", "value": "F"},
    {"children": ["K"], "id": "G", "value": "G"},
    {"children": [], "id": "H", "value": "H"},
    {"children": [], "id": "I", "value": "I"},
    {"children": [], "id": "J", "value": "J"},
    {"children": [], "id": "K", "value": "K"}
  ],
  "startNode": "A"
}


node=Node(name=graph["startNode"])
node.addChild(graph['nodes'])
print(node.children)



    ########################################---- Maximum subset sum with no adjacent element ----#############################################
arrays_algo = Arrays()
sorting_algo = Sorting()
recursion_algo = Recursion()
searching_algo=Searching()
dynamicPrograming_algo=DynamicProgramming()



print('the end')
