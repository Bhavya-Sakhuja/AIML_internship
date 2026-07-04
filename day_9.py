# Array Operations\
import numpy as np 

# arr1 = np.array([1,2,3,4,5])

# print(arr1*2)
# print(arr1+2)
# print(arr1/2)
# print(arr1%2)

arr2 = np.array([2,3,5,1,4,6,6])

# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 % arr2)

# print(arr2[2:4])

# sum() , count() , max() , min() 

# print(arr2.sum())
# print(sum(arr2))
# print(np.sum(arr2))

# print(np.max(arr2))

# print(np.min(arr2))

# # print(np.count(arr2))

print(np.std(arr2))

# print(np.mean(arr2))

# print(np.median(arr2))

# print(np.sort(arr2))

# print(np.unique(arr2))

# arr3 = np.array([1,2])
# arr4 = np.array([3,4])

# # print(np.concatenate((arr3,arr4)))

# print(np.hstack((arr3,arr4)))

# print(np.vstack((arr3,arr4)))
# copy and view 

# arr = np.array([1,2,3,4])

# b = arr.copy()

# b[0] = 78
# print(b)
# print(arr)

# c = arr.view()

# c[1] = 67

# print(c)
# print(arr)


# copy -- call by value 
# view -- call by reference 

# print(arr[arr>1])

# %, / , * , - , +

# list1 = [1,2,3,4,5]

# for i in range(len(list1)):
#     list1[i] += 5

# print(list1)

arr1 = np.array([1,2,3,4,5])

# print(arr1+5)

# print(np.argmax(arr1))
# print(np.argmin(arr1))

# print(np.sqrt(arr1))

# arr = np.array([10,-20,-30])
# print(np.abs(arr))

# round

# arr = np.array([1.34,89.6633])

# print(np.round(arr))

# arryy11 = np.array([[1,2,3],[4,5,6]])

# print(arryy11.flatten())