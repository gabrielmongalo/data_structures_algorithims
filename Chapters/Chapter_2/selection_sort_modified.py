from typing import List

__author__ = 'gmongalo'


class slectionSort:
    def __init__(self, arr = List[int]):
        self.arr = arr

    @property
    def newArr(self) -> List[int]:
        return self.selectSort()


    def selectSort(self) -> List[int]:
        newArr = []
        for i in range(len(self.arr)):
            smallest = self._findSmallest(self.arr)
            newArr.append(self.arr.pop(smallest))
        return newArr


    def _findSmallest(self, arr= List[int]) -> int:
        smallest = arr[0]
        smallest_index = 0
        for i in range(1,len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index


## Todo: I need to make a test Module that will create several lists, sort them and then confirm they are indeed sorted correctly

array_1 = [ 8,45, 87,0, 7]
array_2 = [6,32,7,54,76]
new_array_1 = slectionSort(array_1).newArr
new_array_2 = slectionSort(array_2).newArr
print(f'new_array_1: {new_array_1}')
print(f'new_array_1: {new_array_2}')
