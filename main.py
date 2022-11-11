def duplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(duplicate([1, 2, 1]))
print('Hello World!')
print("Happy Friday!")

