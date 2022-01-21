from black import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i, num in enumerate(nums):
        m = target - num
        print(m)
        if m in dict:
            return[dict[m], i]
        else:
            dict[num] = i
            print(dict)


twoSum(nums = [2, 11, 15, 7], target = 9)
