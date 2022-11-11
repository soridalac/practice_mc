def duplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(duplicate([1, 2, 3, 1, 4, 5]))
