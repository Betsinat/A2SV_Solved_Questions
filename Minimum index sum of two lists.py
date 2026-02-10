class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_idx = float('inf')
        result = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    current = i + j
                    if current < min_idx:
                        min_idx = current
                        result = [list1[i]]
                    elif current == min_idx:
                        result.append(list1[i])
        return result


        
