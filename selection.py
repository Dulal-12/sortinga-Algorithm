
def selection_sort(nums , listSize):
    for i in range (0 , listSize - 1):
     min_index = i
     for j  in range (i + 1 , listSize):
          if nums[j] < nums[min_index]:
               min_index = j
     if min_index != i:
        nums[i] , nums[min_index] = nums[min_index] , nums[i]
    return nums




listSize = int(input('Enter the size of list : '))
nums = []
#user input number
for i in range (listSize) :
    value = int(input("Enter number = "))
    nums.append(value)
sortValue = selection_sort(nums , listSize)
print(sortValue)