# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # this acts as a gate, everything to left is non 0
        gate = 0
        for i in range(len(nums)):
            # if number is non 0, move into gate, shift gate
            if nums[i] != 0:
                # swap values
                nums[i], nums[gate] = nums[gate], nums[i]
                # shift gate by 1
                gate += 1
