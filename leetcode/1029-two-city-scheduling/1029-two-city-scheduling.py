class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[1]-x[0])
        n=len(costs)//2
        s=0
        for i in range(n):
            s+=costs[i][1]
        for i in range(n,len(costs)):
            s+=costs[i][0]
        return s        