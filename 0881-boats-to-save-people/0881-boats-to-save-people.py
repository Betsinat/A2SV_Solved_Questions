class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boats = 0
        left , right = 0 , len(people) - 1
        people.sort()
        while left <= right:
            if people[left] + people[right] > limit:
                right -=1
                boats +=1
            else:
                boats += 1
                left += 1
                right -= 1
        return boats
        