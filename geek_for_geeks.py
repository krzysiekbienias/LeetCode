

#Given an array, find the largest element in it.

class GeeksforGeeks():
    def __init__(self):

        self.m_max_element_unsorted_table=self.max_element()

    def max_element(self,arr):
        the_greatest=arr[0]
        for i in len(arr):
            if arr[i]>the_greatest:
                the_greatest=arr[i]
        return the_greatest



