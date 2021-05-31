#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:59:33 2019
LeetCode
Two sum
@author: yoko
"""

class Solution:
    
    def __init__(self, name):
        self.name = name

    
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[i]+nums[j+1]==target:
                    return [nums[i],nums[j+1]]

sol1 = Solution("1st")
#print(sol1.twoSum([2,7,11,5],9))
#print(sol1.twoSum([2,7,11,5],12))
print(sol1.twoSum([2,7,11,5],16))