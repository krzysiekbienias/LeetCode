from typing import List
import numpy as np
from collections import Counter

class Solution:

#463 Island perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width = len(grid)
        lenght = len(grid[0])
        edges=0
        for i in range(width):
            for k in range(lenght):
                if (grid[i][k]==1):
                    edges+=4
                    if (i+1<=width-1 and grid[i+1][k]==1):#land exist under the one we are
                        edges-=1
                    if (k + 1 <= lenght - 1 and grid[i][k+1] == 1): #land exists on right from the current we are
                        edges -= 1
                    if (k-1>=0  and grid[i][k-1] == 1): #land exists on left from the current we are
                        edges -= 1
                    if (i-1>=0 and grid[i-1][k]==1):
                        edges-=1
        return edges


#832. Flipping an Image

    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        ll_flipped_a=[]
        ll_revert=[]
        f = lambda x: -(x - 1)

        for i in range(len(a)):
            a[i].reverse()
            ll_flipped_a.append(a[i])
        for i in range(len(ll_flipped_a)):
            u=[f(ll_flipped_a[i][k]) for k in range(len(ll_flipped_a[0]))]
            ll_revert.append(u)

        return ll_revert

#657. Robot Return to Origin

    def judgeCircle(self, moves: str) -> bool:
        x=y=0
        for step in moves:
            if(step=='U'):y+=1
            elif (step=='D'):y-=1
            elif (step == 'L'):x-= 1
            elif(step=='R'):x+=1
        dist=np.sqrt(x**2+y**2)
        if dist==0:
            return True
        else :
            return False


# 1002. Find Common Characters

    def commonChars(self, A: List[str]) -> List[str]:
        common_count=Counter(A[0])
        for i in A: #i is a string
            counter=Counter(i)
            common_count &=counter #&= return object common_count keeping only elements also fund in following strings

        return list(common_count.elements())


#476. Number Complement

    def findComplement(self, num: int) -> int:
        l_int_bin=[]
        s_bin=bin(num)[2:]
        l_bin=list(s_bin)
        f = lambda x: -(x - 1)
        for i in range(len(l_bin)):
            temp=int(l_bin[i])
            temp2=str(f(temp))
            l_int_bin.append(temp2)
        s_=''.join(l_int_bin)

        i_decimal_complement=int(s_,2)
        return i_decimal_complement

#860. Lemonade Change
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_notes=0
        ten_notes=0
        twenty_notes=0
        for note in bills:
            if note==5:
                five_notes+=1
            elif note==10:
                five_notes-=1
                ten_notes+=1
            elif note==20 and ten_notes>0:
                ten_notes-=1
                five_notes-=1
                twenty_notes += 1
            elif note==20 and ten_notes==0:
                twenty_notes += 1
                five_notes-=3
            if five_notes<0:
                return False
        return True

#997. Find the Town Judge

#509. Fibonacci Number
    # def fib(self, N: int) -> int:
    #
    #     if N==0:
    #         return 0
    #     elif N=1
    #     result[1]=1
    #     for i in range(1,N):


#561. Array Partition I

    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for i in range(0,len(nums),2):
            result+=nums[i]
        return result

#1029. Two City Scheduling
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        f = lambda x: x[0] - x[1]
        ll_sorted_by_difference=sorted(costs,key=f)
        n=len(costs)//2
        answ=0
        for i in range(n):
            answ+=ll_sorted_by_difference[i][0]+ll_sorted_by_difference[i+n][1]

        return answ

#202. Happy Number
    def isHappy(self, n: int) -> bool:
        mem=set()
        while n!=1:
            n = sum([int(i) ** 2 for i in str(n)]) #very smart
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

# 13. Roman to Integer
    def romanToInt(self, roman: str) -> int:
        dic_transorm={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        int_converted=0
        for i in range(0,len(roman)-1):
            if (dic_transorm[roman[i]]<dic_transorm[roman[i+1]]):
                int_converted-=dic_transorm[roman[i]]
            else:
                int_converted+=dic_transorm[roman[i]]
        int_converted+=dic_transorm[roman[-1]]
        return int_converted


# 169. Majority Element

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        midle_index=len(nums)//2
        return nums[midle_index+1]


# 78. Subsets
    def subsets(self, l_set:List[int]) -> List[List[int]]:
        l_subsets=[[]]
        for ele in l_set:# a list with name set
            for i in range(len(l_subsets)):
                curr_subset=l_subsets[i]
                l_subsets.append(curr_subset+[ele])
        return l_subsets








##############################################################################
##############################################################################

sol=Solution()
#463 Island perimeter
ll_simpler_grid=[[0,1,0],[0,1,0]]
ll_grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
i_perimeter=sol.islandPerimeter(grid=ll_grid)
##############################################################################

#832. Flipping an Image
ll_test=[[1,1,0],[1,0,1],[0,0,0]]
ll_revert=sol.flipAndInvertImage(a=[[1,1,0],[1,0,1],[0,0,0]])
##############################################################################

#657. Robot Return to Origin
s_robot='UDL'
robot=sol.judgeCircle(moves=s_robot)
##############################################################################

# 1002. Find Common Characters
input_ls_common_carr=['mercedes','playstation']
answer_ls_common_carr=sol.commonChars(input_ls_common_carr)
##############################################################################

#476. Number Complement
answer_i_complement=sol.findComplement(num=7)
##############################################################################

#860. Lemonade Change
l_clinents1=[5,5,5,10,5,5,10,20,20,20]#now this work
l_clinents2=[5,5,5,10,20]# this does not work
answer_lemoniade=sol.lemonadeChange(bills=l_clinents2)
##############################################################################

#509. Fibonacci Number
#i_answer_fib=sol.fib(N=6)

#561. Array Partition I
l_partition_1=[1,4,3,2]
answer_partition1=sol.arrayPairSum(nums=l_partition_1)
##############################################################################

#1029. Two City Scheduling
ll_in_cost=[[10,20],[30,200],[10,80],[90,120],[400,50],[30,20]]
i_scheduling_cost=sol.twoCitySchedCost(costs=ll_in_cost)
##############################################################################

#202. Happy Number
b_happy_numbers=sol.isHappy(n=34)
##############################################################################

#13. Roman to Integer
answer=sol.romanToInt(roman='VIII')
##############################################################################

# 169. Majority Element
l_in_majority=[2,2,1,1,1,2,2,5,5,5,5,5] # in this case there is no majority element bo to nie to samo co moda.
# Majority element is the element the element that appears more than n/2
answer_majority=sol.majorityElement(nums=l_in_majority)
##############################################################################

# 78. Subsets
l_in_set=[1,2,3]
answer_subset=sol.subsets(l_set=[1,2,3])
##############################################################################


print("The end")
# def commonChars(self, A: List[str]) -> List[str]:
# 	unique_letters = set(A[0])
# 	result = []
# 	for letter in unique_letters:
# 		counters = []
# 		for word in A:
# 			count = word.count(letter)
# 			if count == 0:
# 				break
# 			counters.append(count)
# 		min_count = min(counters)
# 		while min_count > 0 and len(counters) == len(A):
# 			result.append(letter)
# 			min_count -= 1
# 	return result
