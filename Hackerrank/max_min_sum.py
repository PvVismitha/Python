"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly
four of the five integers. Then print the respective minimum and maximum values
 as a single line of two space-separated long integers.

 Example:
     arr = [1,3,5,7,9]
     op: 16 24

     arr = [1,2,3,4,5]
     op: 10 14

"""

"""
Solution:
1. Calculate the total sum.
2. For max sum, subtract minimum element from total sum
3. For min sum, subtract the maximum element from total sum
"""


def min_max_sum(arr):
    total_sum = arr[0]
    min_ele = arr[0]
    max_ele = arr[0]
    for i in arr[1:]:
        total_sum += i
        min_ele = min(min_ele, i)
        max_ele = max(max_ele, i)

    print(total_sum-max_ele, total_sum-min_ele)


a = [1, 2, 3, 4]
min_max_sum(a)

