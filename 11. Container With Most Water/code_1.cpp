class Solution {
public:
    int maxArea(vector<int>& height) {
        int container = 0;

        int left = 0;
        int right = height.size() - 1;

        while (left < right){
            container = max(container, (right - left) * min(height[left], height[right]));

            if (height[left] == height[right]){
                left += 1;
                right -= 1;
            } else if (height[left] < height[right]){
                left += 1;
            } else {
                right -= 1;
            }
        }

        return container;
    }
};

// O(n) time complexity, O(1) space complexity