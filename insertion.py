def insertion_sort(lst):
    size = len(lst)
    for i in range (1 , size) :
        item = lst[i]
        j = i - 1
        while (j >=0 and lst[j] > item):
            lst[j+1] = lst[j]
            j = j-1
            lst[j+1] = item
    return lst
print(insertion_sort([5,6,7,1,2,3]))