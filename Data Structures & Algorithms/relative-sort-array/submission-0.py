class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        first_ele = arr2[0]
        last_ele = arr2[-1]
        final_list = []
        arr1.sort()
        count1 = Counter(arr1)
        count2 = Counter(arr2)
        for ele in arr2:
            for i in range(count1[ele]):
                final_list.append(ele)
        for ele in arr1:
            if ele >= last_ele and (ele not in arr2 or count1[ele] > count2[ele]):
                final_list.append(ele)
        return final_list