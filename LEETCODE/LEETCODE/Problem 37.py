nums = [0,1,2,2,3,0,4,2]
val = 2


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    index = nums.index(val)
    list_reverse = nums[index:][::-1]
    for i in range(nums.count(val)):
        list_reverse.remove(val)
        nums.remove(val)
    for i in range(len(list_reverse)):
        nums.pop(-i)
    nums += list_reverse
    print(val)
    print(nums)

removeElement(nums, val)