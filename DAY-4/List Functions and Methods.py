nums = [5, 2, 9, 1, 3]

print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

nums.sort()
print("Sorted:", nums)

nums.reverse()
print("Reversed:", nums)

print("Index of 3:", nums.index(3))
print("Count of 2:", nums.count(2))