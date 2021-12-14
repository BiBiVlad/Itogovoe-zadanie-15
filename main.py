def sum_of_pairs(nums):
    if len(nums) % 2 == 0:
        list1 = []
        n = int(len(nums)/2)
        for i in range(0, n):
            a = max(nums)
            nums.remove(a)
            b = min(nums)
            nums.remove(b)
            list1.append(a+b)
        return max(list1)
    else:
        print("Введите четное количество чисел")
print(sum_of_pairs(nums))

