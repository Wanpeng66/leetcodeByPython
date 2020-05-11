from typing import List


class P15(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ll: List[List[int]] = []
        if len(nums) < 3:
            return ll
        length = len(nums)
        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                return ll
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pre = i + 1
            suf = length - 1
            while pre < suf:
                total = nums[i] + nums[pre] + nums[suf]
                if total == 0:
                    ll.append([nums[i], nums[pre], nums[suf]])
                    while pre < suf and nums[pre] == nums[pre+1]:
                        pre += 1
                    while pre < suf and nums[suf] == nums[suf-1]:
                        suf -= 1
                    pre += 1
                    suf -= 1
                elif total > 0:
                    suf -= 1
                else:
                    pre += 1
        return ll

    def method1(self, nums):
        ll: List[List[int]] = []
        if len(nums) < 3:
            return ll
        length = len(nums)
        a = 0
        b = 1
        c = 2
        nums.sort()
        while a <= length - 3 and (nums[a] <= 0):
            if nums[a] + nums[b] + nums[c] == 0:
                tmp: List[int] = [nums[a], nums[b], nums[c]]
                if tmp not in ll:
                    ll.append(tmp)
            if c + 1 <= length - 1:
                c += 1
            elif b + 2 <= length - 1:
                c = b + 2
                b += 1
            else:
                a += 1
                b = a + 1
                c = b + 1
        return ll


if __name__ == '__main__':
    p = P15()
    print(p.threeSum(
        [-6, 14, -11, 7, -5, -8, 12, -13, -3, -14, 7, 0, -7, -15, -5, -9, -13, -7, -5, 9, 8, -13, -6, -8, -12, 7, -10,
         11, 8, -14, 12, 9, -15, -14, 1, -5, -7, -10, -10, 5, -9, 12, 12, -1, 12, 14, -2, -15, -8, 0, 9, 7, 2, 10, 14,
         -3, 2, 11, -6, -13, 12, 13, 11, 5, 14, -11, 7, 14, -6, 12, -4, -7, 9, -7, -1, -1, -8, 4, -9, -9, -11, -15, 5,
         6, 10, 4, 11, -10, -8, 12, -8, -10, 10, 11, 2, 9, -15, -14, 0, -13, 14, 11, -5, 0, -11, 1, 6, -12]))
