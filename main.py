def duplicate(nums):
    hashsets = set()

    for n in nums:
        if n in hashsets:
            return True
        hashsets.add(n)
    return False

print(duplicate([1, 2, 1]))


