arr = [ [1, 2, 3], [4, 5, 6] ]

arr[0].append(7) 

del arr[1][0]

sum_first_list = sum(arr[0])
sum_second_list = sum(arr[1])

arr[0].append(sum_first_list)
arr[1].append(sum_second_list)
