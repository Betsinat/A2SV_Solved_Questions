class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for curr_size in range(len(arr), 1 , -1):
            max_idx = arr.index(curr_size)
            if max_idx == curr_size -1:
                continue
            if max_idx != 0:
                k = max_idx + 1
                res.append(k)
                arr[:k] = arr[:k][::-1]
            res.append(curr_size)
            arr[:curr_size] = arr[:curr_size][::-1]
        return res




        