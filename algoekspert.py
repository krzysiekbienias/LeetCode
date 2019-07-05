class AlgoExpertEasy:
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





easy=AlgoExpertEasy()
print('the end')