import copy


class Sorting:

    unsorted_list = [4, 1, 5, 7, 6, 3, 2, 5, 7, 6, 3, 2]

    def insert_sort(self):
        sorted_list = copy.copy(self.unsorted_list)
        length_list = len(sorted_list)
        for i in range(1, length_list):
            while i > 0 and sorted_list[i - 1] > sorted_list[i]:
                sorted_list[i - 1], sorted_list[i] = sorted_list[i], sorted_list[i - 1]
                i -= 1
        return sorted_list

    def bubble_sort(self):
        sorted_list = copy.copy(self.unsorted_list)
        length_list = len(sorted_list)
        for i in range(1, length_list):
            print(sorted_list)
            for j in range(0, length_list - i):
                if sorted_list[j] > sorted_list[j + 1]:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        return sorted_list

    def choice_sort(self):
        sorted_list = copy.copy(self.unsorted_list)
        length_list = len(sorted_list)
        for i in range(0, length_list - 1):
            for j in range(1 + i, length_list):
                if sorted_list[i] > sorted_list[j]:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        return sorted_list

#print(sorted([4, 1, 5, 7, 6, 3, 2, 5, 7, 6, 3, 2]))
assert Sorting().insert_sort() == sorted([4, 1, 5, 7, 6, 3, 2, 5, 7, 6, 3, 2])
assert Sorting().bubble_sort() == sorted([4, 1, 5, 7, 6, 3, 2, 5, 7, 6, 3, 2])
assert Sorting().choice_sort() == sorted([4, 1, 5, 7, 6, 3, 2, 5, 7, 6, 3, 2])
