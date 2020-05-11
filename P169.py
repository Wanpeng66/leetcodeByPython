from typing import List


class P169(object):
    def majorityElement(self, nums: List[int]) -> int:
        tmp = nums.copy()
        nums = list(set(nums))
        half = len(tmp) / 2

        for i in range(len(nums)):
            if tmp.count(nums[i]) > half:
                return nums[i]


if __name__ == '__main__':
    p = P169()
    print(p.majorityElement([3, 2, 3]))
