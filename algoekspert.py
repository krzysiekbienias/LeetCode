from typing import List


class Arrays:
    def __init__(self):

        self.mli_two_sum = self.two_number_sum(array=[3, 5, -4, 8, 11, 1, -1, 6], target=10)

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

# class Strings:
#     #def __init__(self):
#
#     def cipher_encryptor(self):





arrays_algo = Arrays()
sorting_algo = Sorting()
recursion_algo = Recursion()

print('the end')
