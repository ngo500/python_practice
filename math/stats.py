"""
Module file with functions for getting the mean and median
"""

def mean(nums):
    """
    Takes a list of numbers and returns the mean
    """
    return sum(nums)/len(nums)

def median(nums):
    """
    Takes a list of numbers and returns the median
    """
    nums.sort()

    if(len(nums) % 2 == 0): #if even
        med1 = nums[len(nums) // 2]
        med2 = nums[len(nums) // 2 - 1]
        finalmed = (med1 + med2) / 2
    else: #else not even
        finalmed = nums[len(nums) // 2]
  
    return finalmed
