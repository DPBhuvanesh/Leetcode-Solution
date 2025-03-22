class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element = set()

        for x in nums:
            if x in element:
                return True
            element.add(x)

        return False