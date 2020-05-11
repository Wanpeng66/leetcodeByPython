from typing import List


class P41(object):

    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x > 0, list(set(nums))))
        if len(nums) == 0:
            return 1
        nums.sort()
        for i in range(1, len(nums) + 1):
            if nums[i - 1] != i:
                return i
        return nums[len(nums) - 1] + 1


if __name__ == '__main__':
    p = P41()
    print(p.firstMissingPositive([0, 2, 2, 1, 1]))
