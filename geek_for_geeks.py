# Given an array, find the largest element in it.



class GeeksforGeeks():
    def __init__(self):

        self.m_max_element_unsorted_table = self.max_element(arr=[3, 5, 6, 1, 2, 8, 10, 15])
        self.mb_equals_arr = self.equal_arrays(arr1=[2, 5, 6, 9, 1], arr2=[9, 1, 2, 6, 5])

    def max_element(self, arr):
        the_greatest = arr[0]
        for i in range(len(arr)):
            if arr[i] > the_greatest:
                the_greatest = arr[i]
        return the_greatest

    # Check if two arrays are equal or not
    # Given two given arrays of equal length, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements
    # (or permutation) of elements may be different though.
    # If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

    def equal_arrays(self, arr1, arr2):

        l = len(arr1)
        k = len(arr2)
        if l != k:
            return False
        else:
            arr1.sort()
            arr2.sort()
            for i in range(k):
                if arr1[i] != arr2[i]:
                    return False
            else:
                 return True




        # return    [True if arr1[i]== arr2[i] else  False for i in range(k)]


gfg = GeeksforGeeks()
print(-float('inf'))
print('the end')
