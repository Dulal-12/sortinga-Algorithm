def selection_sort(nums) : 
    size = len(nums)
    for i in range(0 , size-1):
        min_pos = i
        for j in range (i+1 , size):
            if nums[j] < nums[min_pos] :
                min_pos = j
        if min_pos != i:
            nums[i] , nums[min_pos] = nums[min_pos] , nums[i]
    return nums


sortValue = selection_sort([4,3,2,1,8,9,6])
print(sortValue)