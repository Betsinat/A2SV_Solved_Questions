#include <vector>
#include <algorithm>
class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int startValue = 1; 
        bool found = false;
        while (!found) {
            found = true;
            int current = startValue;
            for (int num : nums) {
                current += num;
                if (current < 1) {
                    found = false;
                    startValue++;
                    break;
                }
            }
        }
        return startValue;
    }
};
