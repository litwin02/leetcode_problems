nums = [-2, -1, 1, 4]

min_number = nums[0]
min_value = abs(nums[0])

for n in nums:
    if abs(n) < min_value:
        min_number = n
        min_value = abs(n)
    elif abs(n) == min_value and n > min_number:
        min_number = n

print(min_number)