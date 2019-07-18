from typing import List
import numpy as np
from collections import Counter


class Strings:
    def __init__(self):
        self.mf_robot = self.judgeCircle(moves='UUDR')
        self.mls_common_carr = self.commonChars(A=['mercedes', 'playstation'])
        self.m_roman_converted = self.romanToInt(roman='VIII')  # 657
        self.mint_first_non_repetingch = self.first_non_repeting_char(s="aadaada")
        self.ml_thirdword = self.findOcurrences(text="we will we will rock you", first="we", second="will")  # 1078
        self.mb_anagram = self.isAnagram(s='anagram', t='nagaram')
        self.mb_patern = self.wordPattern(pattern='abba', words='dog cat cat dog')
        self.m_len_of_last_word = self.lengthOfLastWord(s='a ')
        self.m_ransom_note=self.canConstruct(ransomNote='aa', magazine='ab')
        self.m_ransom_note_count=self.canConstruct_using_count(ransomNote='fffbfg', magazine="effjfggbffjdgbjjhhdegh")
        self.m_ransom_note_count=self.canConstruct_using_dict(ransomNote='fffbfg', magazine="effjfggbffjdgbjjhhdegh")




    def canConstruct(self, ransomNote: str, magazine: str) -> bool:#does not work for ransome='aa', magaizne='ab'
            l_ransom_note = list(ransomNote)
            l_magazin = list(magazine)
            b_results=all(ch in l_magazin for ch in l_ransom_note)
            return b_results

    def canConstruct_using_count(self, ransomNote: str, magazine: str) -> bool: #does not work
        i_number_of_substrings=magazine.count(ransomNote)
        if i_number_of_substrings==0:
            return False
        else:
            return True
    #dictionary approach

    def canConstruct_using_dict(self, ransomNote: str, magazine: str) -> bool:
        dic_magaz={}
        dic_ransom={}

        for ch in magazine:
            dic_magaz[ch]=dic_magaz.get(ch,0)+1
        for ch in ransomNote:
            dic_ransom[ch]=dic_ransom.get(ch,0)+1
        return False





    def merge_alternatively(self, s1, s2):
        result = ""
        s1_split = list(s1)
        s2_split = list(s2)
        len_s1 = len(s1_split)
        len_s2 = len(s2_split)
        if (len_s1 >= len_s2):
            for i in range(len_s2):
                s1_split.insert(2 * i + 1, s2_split[i])
            result = "".join(s1_split)
        else:
            for i in range(len_s1):
                s2_split.insert(2 * i, s1_split[i])
            result = "".join(s2_split)
        return result

    # 657. Robot Return to Origin

    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for step in moves:
            if (step == 'U'):
                y += 1
            elif (step == 'D'):
                y -= 1
            elif (step == 'L'):
                x -= 1
            elif (step == 'R'):
                x += 1
        dist = np.sqrt(x ** 2 + y ** 2)
        if dist == 0:
            return True
        else:
            return False

        # 387. First Unique Character in a String

    def first_non_repeting_char(self, s):
        if s == "":
            return -1
        elif len(s) == 1:
            return 0
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
            l_chfrequency = list(dic.values())
        if 1 not in l_chfrequency:
            return -1
        for ch in s:
            if dic[ch] == 1:
                first_ch = ch
                index_of_first_ch = s.index(first_ch)
                return index_of_first_ch

        # 1002. Find Common Characters

    def commonChars(self, A: List[str]) -> List[str]:
        common_count = Counter(A[0])
        for i in A:  # i is a string
            counter = Counter(i)
            common_count &= counter  # &= return object common_count keeping only elements also fund in following strings

        return list(common_count.elements())

        # 13. Roman to Integer

    def romanToInt(self, roman: str) -> int:
        dic_transorm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_converted = 0
        for i in range(0, len(roman) - 1):
            if (dic_transorm[roman[i]] < dic_transorm[roman[i + 1]]):
                int_converted -= dic_transorm[roman[i]]
            else:
                int_converted += dic_transorm[roman[i]]
        int_converted += dic_transorm[roman[-1]]
        return int_converted

    # 1078. Occurrences After Bigram

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        l_splited_text = text.split()
        mapping = {}
        for i in range(len(l_splited_text) - 2):
            t_key = (l_splited_text[i], l_splited_text[i + 1])
            mapping.setdefault(t_key, []).append(l_splited_text[i + 2])
        current_keys = (first, second)
        if current_keys not in mapping:
            return []
        return mapping[current_keys]

    # 242. Valid Anagram

    def isAnagram(self, s: str, t: str) -> bool:
        dics = {}
        dict = {}
        if len(s) != len(t):
            return False
        for ch in s:
            dics[ch] = dics.get(ch, 0) + 1
        for ch2 in t:
            dict[ch2] = dict.get(ch2, 0) + 1
        if dics == dict:
            return True
        else:
            return False

    # 290. Word Pattern
    # hint check if there is a bijection between values of dictionaries
    def wordPattern(self, pattern: str, words: str) -> bool:
        dic_pattern = {}
        dic_words = {}
        l_words = words.split(' ')
        for ch in pattern:
            dic_pattern[ch] = dic_pattern.get(ch, 0) + 1
        l_values = list(dic_pattern.values())
        for i in l_words:
            dic_words[i] = dic_words.get(i, 0) + 1
        l_words = list(dic_words.values())
        if l_values == l_words:
            return True
        else:
            return False

    # 58. Length of Last Word
    def lengthOfLastWord(self, s: str) -> int:  # does not work for 'a '
        if (len(s) == 1 and s != " "):
            return 1
        elif (s == ' ' or s == ''):
            return 0
        l_words = s.split(' ')
        last_word = l_words[-1]
        return len(last_word)


class Arrays:
    def __init__(self):
        self.m_perimeter = self.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])  # 463
        self.mll_revert = self.flipAndInvertImage(a=[[1, 1, 0], [1, 0, 1], [0, 0, 0]])  # 832
        self.m_lemoniade = self.lemonadeChange(bills=[5, 5, 5, 10, 5, 5, 10, 20, 20, 20])  # 860
        self.m_partition1 = self.arrayPairSum(nums=[1, 4, 3, 2])
        self.i_scheduling_cost = self.twoCitySchedCost(
            costs=[[10, 20], [30, 200], [10, 80], [90, 120], [400, 50], [30, 20]])
        self.m_majority = self.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2, 5, 5, 5, 5, 5])  # 169
        self.m_int_single_numb = self.singleNumber(nums=[1, 2, 1, 2, 4])
        self.m_duplicators = self.containsDuplicate(a_list=[3, 6, 7, 3, 3, 5])
        #self.m_without_duplicates = self.removeDuplicates(a_list=[3,3, 4,5,7,7,8,8,10])
        self.m_zero_push = self.moveZeroes([0, 1, 0, 3, 12])

     #27. Remove Element

    # 283. Move Zeroes
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(u=i, w=pointer, array=nums)
                pointer += 1

    def swap(self, u, w, array):
        array[u], array[w] = array[w], array[u]

    # 26. Remove Duplicates from Sorted Array
    # def removeDuplicates(self, a_list: List[int]) -> int:
    #     l = len(a_list)
    #     for i in range(l-1):
    #         if a_list[i] == a_list[i + 1]:
    #             del a_list[i]
    #             l-=1
    #     return l



    #variation of 217 where we are supposed to
    def containsDuplicate(self, a_list: List[int]) -> bool:
        l = len(a_list)
        if (l < 2):
            return False
        a_list.sort()
        for i in range(l - 1):
            if a_list[i] == a_list[i + 1]:
                return True
        return False

    # 463 Island perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width = len(grid)
        lenght = len(grid[0])
        edges = 0
        for i in range(width):
            for k in range(lenght):
                if (grid[i][k] == 1):
                    edges += 4
                    if (i + 1 <= width - 1 and grid[i + 1][k] == 1):  # land exist under the one we are
                        edges -= 1
                    if (k + 1 <= lenght - 1 and grid[i][
                        k + 1] == 1):  # land exists on right from the current we are
                        edges -= 1
                    if (k - 1 >= 0 and grid[i][k - 1] == 1):  # land exists on left from the current we are
                        edges -= 1
                    if (i - 1 >= 0 and grid[i - 1][k] == 1):
                        edges -= 1
        return edges

        # 832. Flipping an Image

    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        ll_flipped_a = []
        ll_revert = []
        f = lambda x: -(x - 1)

        for i in range(len(a)):
            a[i].reverse()
            ll_flipped_a.append(a[i])
        for i in range(len(ll_flipped_a)):
            u = [f(ll_flipped_a[i][k]) for k in range(len(ll_flipped_a[0]))]
            ll_revert.append(u)

        return ll_revert

        # 860. Lemonade Change

    def lemonadeChange(self, bills: List[int]) -> bool:
        five_notes = 0
        ten_notes = 0
        twenty_notes = 0
        for note in bills:
            if note == 5:
                five_notes += 1
            elif note == 10:
                five_notes -= 1
                ten_notes += 1
            elif note == 20 and ten_notes > 0:
                ten_notes -= 1
                five_notes -= 1
                twenty_notes += 1
            elif note == 20 and ten_notes == 0:
                twenty_notes += 1
                five_notes -= 3
            if five_notes < 0:
                return False
        return True

        # 561. Array Partition I

    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

        # 1029. Two City Scheduling

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        f = lambda x: x[0] - x[1]
        ll_sorted_by_difference = sorted(costs, key=f)
        n = len(costs) // 2
        answ = 0
        for i in range(n):
            answ += ll_sorted_by_difference[i][0] + ll_sorted_by_difference[i + n][1]

        return answ

    # 169. Majority Element

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        midle_index = len(nums) // 2
        return nums[midle_index + 1]

    # 136. Single Number

    def singleNumber(self, nums: List[int]):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        list_of_items = list(dic.items())
        for item in list_of_items:
            if item[1] == 1:
                return item[0]

        return list_of_items


class Searching:
    def __init__(self):
        self.m_bin_search = self.search(l_array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target=33)  # 704

        # 704. Binary Search (runtime error for leetcode)#solution from

    def binary_search_helper(self, l_array, target, left, right):
        if left > right:
            return -1

        middle = (left + right) // 2
        potential_match = l_array[middle]
        if target == potential_match:
            return [middle]
        elif target < potential_match:
            return self.binary_search_helper(l_array, target, left, middle - 1)

        else:
            return self.binary_search_helper(l_array, target, middle + 1, right)

    def search(self, l_array: List[int], target: int) -> int:
        return self.binary_search_helper(l_array, target, 0, len(l_array) - 1)[0]


class Math:
    def __init__(self):
        self.m_subsets = self.subsets(l_set=[1, 2, 3])  # 78
        self.mf_pow = self.myPow(x=2, n=4)
        self.b_happy_numbers = self.isHappy(n=34)  # 202
        self.mb_is_int_palin = self.isPalindrome(x=1)  # 9
        self.mi_complement = self.findComplement(num=7)  # 476
        self.m_int_of_sqr=self.mySqrt(x=21)

    # 69. Sqrt(x)
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        while left<=right:
            mid=(left+right)//2
            mid_sqr=mid*mid
            if mid_sqr>x:
                right=mid-1
            else:
                left=mid+1
        return left -1


    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1
        res = self.myPow(x, n // 2)
        res = res * res
        return res

        # 78. Subsets

    def subsets(self, l_set: List[int]) -> List[List[int]]:
        l_subsets = [[]]
        for ele in l_set:  # a list with name set
            for i in range(len(l_subsets)):
                curr_subset = l_subsets[i]
                l_subsets.append(curr_subset + [ele])
        return l_subsets

    # 202. Happy Number
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])  # very smart
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

    # 9.Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    def isPalindrome(self, x: int) -> bool:  # 11504 / 11509 test cases passed.  issue for x=1000021
        b_status = False
        if x < 0:
            return b_status
        elif x == 0:
            b_status = True
            return b_status
        else:

            l_x = list(str(x))  # list of x
            l_x_reverse = l_x[::-1]
            for i in range(len(l_x)):
                if len(l_x) == 1:
                    return True
                elif l_x[0] != l_x[-1]:
                    b_status = False
            else:
                if (l_x[i] == l_x_reverse[i] and l_x[-1] != '0'):
                    b_status = True
        return b_status

    # 476. Number Complement

    def findComplement(self, num: int) -> int:
        l_int_bin = []
        s_bin = bin(num)[2:]
        l_bin = list(s_bin)
        f = lambda x: -(x - 1)
        for i in range(len(l_bin)):
            temp = int(l_bin[i])
            temp2 = str(f(temp))
            l_int_bin.append(temp2)
        s_ = ''.join(l_int_bin)

        i_decimal_complement = int(s_, 2)
        return i_decimal_complement


class DynamicProgramming:
    def __init__(self):
        self.m_house_rober = self.rob(nums=[1, 3, 1])

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        elif len(nums) > 2:
            total_robbed = [0] * len(nums)
            total_robbed[0] = nums[0]
            total_robbed[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                total_robbed[i] = max(nums[i] + total_robbed[i - 2], total_robbed[i - 1])
            return total_robbed[-1]


######################################----SOLUTIONS----#####################################################
strings_lc = Strings()
arrays_lc = Arrays()
searching_lc = Searching()
math_lc = Math()
dynamic_prog_lc = DynamicProgramming()

print("The end")
