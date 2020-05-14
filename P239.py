from typing import List


class P239(object):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res: list[int] = []
        size = len(nums)
        for i in range(size - k + 1):
            tmp = nums[i: i + k]
            if len(res) == 0 or res[-1] == nums[i-1]:
                tmp.sort()
                res.append(tmp[-1])
            else:
                res.append(max(res[-1], tmp[-1]))
        return res


if __name__ == '__main__':
    p = P239()
    print(p.maxSlidingWindow([7, 2, 4], 2))
