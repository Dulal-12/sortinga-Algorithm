# def even_last(lst):
#     index = []
#     for i in range (len(lst)) :
#         if i % 2 == 0 :
#             index.append(lst[i])
#     countValue = lst[-1];
#     newValue = list(map(lambda a : a * countValue , index))
#     return sum(newValue)

# print(even_last([1, 3, 3, 1, 10]) )

def bubble_sort(lst) :
    size = len(lst)
    for i in range (size):
        for j in range (0 , size-1-i):
            if lst[j] > lst[j+1] :
                lst[j] , lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubble_sort([9,6,5,4,3,3]))