nums = list(map(int, input().split()))

idex = nums.index(0)

result = nums[idex-1] + nums[idex-2]+nums[idex-3]
print(result)