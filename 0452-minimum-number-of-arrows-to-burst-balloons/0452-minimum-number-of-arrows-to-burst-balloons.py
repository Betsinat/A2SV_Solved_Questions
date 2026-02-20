class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        curr_end =  points[0][1]
        for start , end in points[1:]:
            if start > curr_end:
                arrows += 1
                curr_end =  end
            else:
                curr_end= min(curr_end , end)
        return arrows

        


       


        