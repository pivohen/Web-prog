#массивы/списки

arr_1 = [1, 23, 561, 5, 6]

print(
    arr_1,
    arr_1[0], # first element
    arr_1[-1], # last element
    len(arr_1), # count elements
)

# if len(arr_1) > 0:
#     print(
#         rr_1[len(arr_1) - 1], # last element of arr
#     )
# else:
#     print('Empty')

arr_2 = [
    "str", 12, 3, 4.22, 2, arr_1,
]


arr_2.append(88) # add elem in end of array

del arr_2[0] # delete elem [index]
arr_2.remove(12) # delete elem (по значению)


print(arr_2)


#цикл for

for a in arr_2:
    print(
        f'{a} has type {type(a)}',
    )
    #print(a)



print(id(arr_1))
