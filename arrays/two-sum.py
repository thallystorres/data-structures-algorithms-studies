def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for index in range(len(nums)):
        d[nums[index]] = index
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d and d[complement] != i:
            return [i, d[complement]]
    return []