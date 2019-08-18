from typing import List
import numpy as np
from collections import Counter


class Strings:
    def __init__(self):
        ############################################---- ----#########################################################
        self.mf_robot = self.judgeCircle(moves='UUDR')
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.mls_common_carr = self.commonChars(A=['mercedes', 'playstation'])
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.m_roman_converted = self.romanToInt(roman='VIII')  # 657
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.mint_first_non_repetingch = self.first_non_repeting_char(s="aadaada")
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.ml_thirdword = self.findOcurrences(text="we will we will rock you", first="we", second="will")  # 1078
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.mb_anagram = self.isAnagram(s='anagram', t='nagaram')
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.mb_patern = self.wordPattern(pattern='abba', words='dog cat cat dog')
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.m_len_of_last_word = self.lengthOfLastWord(s='a ')
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.m_ransom_note = self.canConstruct(ransomNote='aa', magazine='ab')
        self.m_ransom_note_count = self.canConstruct_using_count(ransomNote='fffbfg', magazine="effjfggbffjdgbjjhhdegh")
        self.m_ransom_note_dict = self.canConstruct_using_dict(ransomNote='fffbfg', magazine="effjfggbffjdgbjjhhdegh")
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.mlint_large_group = self.largeGroupPositions(S='aaa')
        ############################################---- ----#########################################################

        ############################################---- ----#########################################################
        self.groups = self.strings_splits(s='110001111000000')
        self.m_substrings = self.countBinarySubstrings(s='110001111000000')
        ############################################---- ----#########################################################

    #######################################---- 696. Count Binary Substrings----################################
    # helper function that split strings into groups
    def strings_splits(self, s: str) -> List[int]:
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        return groups

    def countBinarySubstrings(self, s: str) -> int:
        groups = self.strings_splits(s=s)
        res = 0
        for i in range(1, len(groups)):
            res += min(groups[i - 1], groups[i])
        return res

    #######################################---- 696. Count Binary Substrings----################################

    #######################################---- 830. Positions of Large Groups----################################
    # helper function to get key based on value. It does not help

    def getKeysByValue(self, dict, target_value: int, condition: str) -> List[int]:
        l_listOfKeys = []
        l_listOfItems = list(dict.items())  # It needs to be casted on list because'dict_items' object
        # does not support indexing
        for item in l_listOfItems:
            if condition == 'equal':
                if item[1] == target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'graterOrEqual':
                if item[1] >= target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'grater':
                if item[1] > target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'less':
                if item[1] < target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'lessOrEqual':
                if item[1] <= target_value:
                    l_listOfKeys.append(item[0])
        return l_listOfKeys

    def largeGroupPositionsNotFinished(self, S: str) -> List[
        List[int]]:  # using this approach it would be hard to get what we want
        d_box = {}
        for ch in S:
            d_box[ch] = d_box.get(ch, 0) + 1
        d_large_group = self.getKeysByValue(dict=d_box, target_value=3, condition='graterOrEqual')

    def largeGroupPositions(self, S: str) -> List[List[int]]:
        groups = []
        beg = 0
        end = 0
        while end < len(S):
            if S[end] != S[beg]:
                if end - beg >= 3:
                    groups.append([beg, end - 1])
                beg = end
            else:
                end += 1
        if end - beg >= 3:
            groups.append([beg, end - 1])
        return groups

    #######################################---- 830. Positions of Large Groups----################################

    #######################################---- 383 Ransom Note----################################
    # 383 Ransom Note
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  # does not work for ransome='aa', magaizne='ab'
        l_ransom_note = list(ransomNote)
        l_magazin = list(magazine)
        b_results = all(ch in l_magazin for ch in l_ransom_note)
        return b_results

    def canConstruct_using_count(self, ransomNote: str, magazine: str) -> bool:  # does not work
        i_number_of_substrings = magazine.count(ransomNote)
        if i_number_of_substrings == 0:
            return False
        else:
            return True

    # dictionary approach-Accepted

    def canConstruct_using_dict(self, ransomNote: str, magazine: str) -> bool:
        dic_magaz = {}
        dic_ransom = {}
        for ch in magazine:
            dic_magaz[ch] = dic_magaz.get(ch, 0) + 1
        for ch in ransomNote:
            dic_ransom[ch] = dic_ransom.get(ch, 0) + 1
        for letter in dic_ransom:
            if letter not in dic_magaz:
                return False
            else:
                if dic_magaz[letter] < dic_ransom[
                    letter]:  # if in magazin is less number of specific letter also we are not
                    # able to construct ransom notice
                    return False
        return True

    #######################################---- 383 Ransom Note----################################

    #######################################---- Merge Alternatively----################################
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

    #######################################---- Merge Alternatively----################################

    #######################################---- 3657. Robot Return to Origin ---################################

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

    #######################################---- 3657. Robot Return to Origin ---################################

    #######################################---- 387. First Unique Character in a String ---################################
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

    #######################################---- 387. First Unique Character in a String ---################################

    #######################################---- 1002. Find Common Characters ---################################

    def commonChars(self, A: List[str]) -> List[str]:
        common_count = Counter(A[0])
        for i in A:  # i is a string
            counter = Counter(i)
            common_count &= counter  # &= return object common_count keeping only elements also fund in following strings
        return list(common_count.elements())

    #######################################---- 1002. Find Common Characters ---################################

    #######################################---- 13. Roman to Integer ---################################

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

    #######################################---- 13. Roman to Integer ---################################

    #######################################---- 1078. Occurrences After Bigram ---################################

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

    #######################################---- 1078. Occurrences After Bigram ---################################

    #######################################---- 242. Valid Anagram ---################################

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

    #######################################---- 242. Valid Anagram ---################################

    #######################################---- 290. Word Pattern ---################################
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

    #######################################---- 290. Word Pattern ---################################

    #######################################---- 58. Length of Last Word ---################################

    def lengthOfLastWord(self, s: str) -> int:  # does not work for 'a '
        if (len(s) == 1 and s != " "):
            return 1
        elif (s == ' ' or s == ''):
            return 0
        l_words = s.split(' ')
        last_word = l_words[-1]
        return len(last_word)
    #######################################---- 58. Length of Last Word ---################################


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
        self.m_without_duplicates = self.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        self.m_zero_push = self.moveZeroes([0, 1, 0, 3, 12])
        self.mlintFirstEven = self.sortArrayByParity(A=[3, 1, 2, 4])
        self.mlintSquares = self.sortedSquares(A=[-4, -1, 0, 3, 10])
        self.mintHighCheck = self.heightChecker(heights=[2, 1, 2, 1, 1, 2, 2, 1])
        self.mAfterRemovingElement=self.removeElement([0,1,2,2,3,0,4,2],val=2)


    #######################################---- 27. Remove Elements----################################
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
    #######################################---- 27. Remove Elements----################################


    #######################################---- 1051. Height Checker----################################
    def heightChecker(self, heights: List[int]) -> int:  # brute force
        wrong_standing = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                if heights[i] > heights[j]:
                    wrong_standing += 1
        return wrong_standing

    #######################################---- 1051. Height Checker----################################

    #######################################---- 977. Squares of a Sorted Array ----################################
    def sortedSquares(self, A: List[int]) -> List[int]:
        squared = lambda x: x ** 2
        results = list(map(squared, A))
        results.sort()
        return results

    #######################################---- 977. Squares of a Sorted Array----################################

    #######################################---- 905. Sort Array By Parity ----################################
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l_even = []
        l_odd = []
        for i in A:
            if i % 2 == 0:
                l_even.append(i)
            else:
                l_odd.append(i)
        return l_even + l_odd
        #######################################---- 905. Sort Array By Parity ----################################

    #######################################---- 283. Move Zeroes ----################################
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(u=i, w=pointer, array=nums)
                pointer += 1

    def swap(self, u, w, array):
        array[u], array[w] = array[w], array[u]

    #######################################---- 283. Move Zeroes ----################################

    # 26. Remove Duplicates from Sorted Array
    # Wrong Approach!! It is not a good idea to change a list while iterating through it. It gives index out of range.
    # def removeDuplicates(self, a_list: List[int]) -> int:
    #     l = len(a_list)
    #     for i in range(l-1):
    #         if a_list[i] == a_list[i + 1]:
    #             del a_list[i]
    #             l-=1
    #     return l

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)

    # variation of 217 where we are supposed to
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
        self.m_int_of_sqr = self.mySqrt(x=21)
        self.mb_pow_of3 = self.isPowerOfThree(n=9)
        self.mint_reach = self.reachNumber(target=2)
        self.mbol_perfect_number = self.checkPerfectNumber(num=8128)
        self.l_divisors = self.all_divisors_with_sqrt(10 ** 10)
        self.mb_isBoom = self.isBoomerang(points=[[0, 0], [0, 2], [2, 1]])
        self.mlint_errorNumber = self.findErrorNums(nums=[3, 2, 2])
        self.mlintDividing = self.selfDividingNumbers(left=1, right=12)
        self.mb_selfDividing = self.CheckSingleNumber('128')




      ##########################################################################################################
    ##################################----FUNCTIONS----######################################################
    ##########################################################################################################

    #######################################---- 728. Self Dividing Numbers ----################################
    # helper number
    def CheckSingleNumber(self, aStr):
        b_status = True
        ls_digits = list(aStr)
        for i in ls_digits:
            if int(i) == 0:
                b_status = False

            elif (int(i) != 0 and int(aStr) % int(i) != 0):
                b_status = False

        return b_status

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        i = left
        l_selfDividingNum = []
        while i <= right:
            str_converted = str(i)
            b_temp = self.CheckSingleNumber(str_converted)
            if b_temp == True:
                l_selfDividingNum.append(i)
            i += 1

        return l_selfDividingNum

    #######################################---- 728. Self Dividing Numbers ----################################

    #######################################---- 645. Set Mismatch ----################################
    def getKeysByValue(self, dict, target_value: int, condition: str) -> List[int]:
        l_listOfKeys = []
        l_listOfItems = list(dict.items())  # It needs to be casted on list because'dict_items' object
        # does not support indexing
        for item in l_listOfItems:
            if condition == 'equal':
                if item[1] == target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'graterOrEqual':
                if item[1] >= target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'grater':
                if item[1] > target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'less':
                if item[1] < target_value:
                    l_listOfKeys.append(item[0])
            if condition == 'lessOrEqual':
                if item[1] <= target_value:
                    l_listOfKeys.append(item[0])
        return l_listOfKeys

    def findErrorNums(self, nums: List[int]) -> List[int]:  # 7 / 49 test cases passed. First problem with [2,2]
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        duplicated_number = self.getKeysByValue(dict=d, target_value=2, condition='equal')
        if len(nums) == 2:
            if duplicated_number[0] == 1:
                return [duplicated_number[0], duplicated_number[0] + 1]
            else:
                return [duplicated_number[0], 1]
        else:
            missing_number = duplicated_number[0] + 1
        return [duplicated_number[0], missing_number]

    #######################################---- 645. Set Mismatch ----################################

    #######################################---- 1037. Valid Boomerang ----################################
    def isBoomerang(self, points: List[List[int]]) -> bool:
        l_aParameters = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                try:
                    a = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                except ZeroDivisionError:
                    a = float('-inf')
                l_aParameters.append(a)
        se = set(l_aParameters)
        if len(se) == len(points):
            return True
        else:
            return False

    #######################################---- 1037. Valid Boomerang ----################################

    #######################################---- 754 Reach a Number ----################################
    # 754 Reach a Number
    def reachNumber(self, target: int) -> int:  # TLE i think that due to this while loop to find n
        if target < 0:
            target = - target
        l_numbers = []
        i = 1
        partial_sum = sum(l_numbers)
        while partial_sum < target:
            l_numbers.append(i)
            i += 1
            partial_sum = sum(l_numbers)
        n = l_numbers[-1]
        to_substract = partial_sum - target
        if to_substract % 2 == 0:  # missng part is even
            return n  # 1+2+3+...+i+...+n. we only need to replace i on -i
        elif to_substract % 2 == 1 and (n + 1) % 2 == 1:
            return n + 1
        elif to_substract % 2 == 1 and (n + 1) % 2 == 0:
            return n + 2

    # 754 Reach a Number variant 2
    def reachNumber_using_n_approxim(self,
                                     target: int) -> int:  # it does not work wrong answer for target =3 and only 13/73
        if target < 0:
            target = - target
        n = math.floor(math.sqrt(target))
        partial_sum = n * (n + 1) / 2
        to_substract = partial_sum - target
        if to_substract % 2 == 0:  # missng part is even
            return n  # 1+2+3+...+i+...+n. we only need to replace i on -i
        elif to_substract % 2 == 1 and (n + 1) % 2 == 1:
            return n + 1
        elif to_substract % 2 == 1 and (n + 1) % 2 == 0:
            return n + 2

    #######################################---- 754 Reach a Number ----################################

    ##########################################################################################################

    #######################################---- 507. Perfect Number ----################################

    # 507. Perfect Number

    # helper functions
    def all_divisors(self, number):
        l_divisors = []
        for i in range(1, number):
            if number % i == 0:
                l_divisors.append(i)
        return l_divisors

    def all_divisors_with_sqrt(self, number):  # more optimal solution without last divisor.
        l_divisors = []
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                l_divisors.append(i)
                l_divisors.append(int(number / i))
        return [1] + l_divisors

    def checkPerfectNumber(self, num: int) -> bool:  # TLE 45 / 156 test cases passed.
        int_divisorsSum = sum(self.all_divisors_with_sqrt(number=num))
        if int_divisorsSum == num:
            return True
        else:
            return False

    def checkPerfectNumberAccepted(self, num: int) -> bool:
        if num < 0:
            return False
        if num == 1:
            return False
        int_divisorsSum = sum(self.all_divisors_with_sqrt(number=num))
        if int_divisorsSum == num:
            return True
        else:
            return False

    #######################################---- 507. Perfect Number ----################################

    #######################################---- Power of Three ----################################
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return True
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            mid_cube = mid * mid * mid
            if n == mid_cube:
                return True
            if mid_cube > n:
                right = mid - 1
            else:
                left = mid + 1
        return False

    #######################################---- Power of Three ----################################

    #######################################---- 69. Sqrt(x) ----################################
    # 69. Sqrt(x)
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            mid_sqr = mid * mid
            if mid_sqr > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1

    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1
        res = self.myPow(x, n // 2)
        res = res * res
        return res

        #######################################---- 69. Sqrt(x) ----################################

        #######################################---- 78. Subsets ----################################

        # 78. Subsets

    def subsets(self, l_set: List[int]) -> List[List[int]]:
        l_subsets = [[]]
        for ele in l_set:  # a list with name set
            for i in range(len(l_subsets)):
                curr_subset = l_subsets[i]
                l_subsets.append(curr_subset + [ele])
        return l_subsets


    #######################################---- 78. Subsets ----################################
    #######################################---- 202. Happy Number ----################################

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
        #######################################---- 202. Happy Number ----################################

        #######################################---- # 9. Palindrome ----################################

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

        #######################################---- 9. Palindrome ----################################

        #######################################---- 476. Number Complement ----################################

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
    #######################################---- 476. Number Complement ----################################


class DynamicProgramming:
    def __init__(self):
        self.m_house_rober = self.rob(nums=[1, 3, 1])
        self.mi_min_coins_number = self.coinChange(coins=[2], amount=3)

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

    def coinChange(self, coins: List[int], amount: int) -> int:
        l_dp = [float('inf')] * (amount + 1)
        l_dp[0] = 0
        for x in range(1, amount + 1):
            for coin in coins:
                if x >= coin:
                    l_dp[x] = min(l_dp[x], 1 + l_dp[x - coin])
        if l_dp[amount] == float('inf'):
            return -1
        return l_dp[amount]



class Recursion:
      def __init__(self):
          self.mSubsets=self.helperSubsets(nums=[1,2,3])

          # algoexpert version, needs to be tailored for leetcode

      # def powerset(self, array, idx=None):  # recursive
      #     if idx is None:
      #         idx = len(array) - 1
      #     elif idx < 0:
      #         return [[]]
      #     ele = array[idx]
      #     subsets = self.powerset(array, idx - 1)
      #     for i in range(len(subsets)):
      #         current_subset = subsets[i]
      #         subsets.append(current_subset + [ele])
      #     return subsets

      def helperSubsets(self, nums,idx=None):  # recursive
          if idx is None:
              idx = len(nums) - 1
          elif idx < 0:
              return [[]]
          ele = nums[idx]
          subsets = self.helperSubsets(nums,idx-1)
          return subsets



######################################----SOLUTIONS----#####################################################
strings_lc = Strings()
arrays_lc = Arrays()
searching_lc = Searching()
math_lc = Math()
dynamic_prog_lc = DynamicProgramming()
recursion=Recursion()

print("The end")
