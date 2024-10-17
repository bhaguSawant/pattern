#Remove Duplicates Numbers

# method 1: By using set
# arr=[2,4,3,2,2,1,4,3,2,5,6,5,6,7,8]
# arr2=set(arr)  # if i want in list then use \\arr2=list(set(arr))\\
# print(arr2)

#----------------------------------------------------------------------

# method 2: By using for loop
arr=[2,4,3,2,2,1,4,3,2,5,6,5,6,7,8]
arr2=[]
for i in arr:
    if i not in arr2:
        arr2.append(i)
print(arr2)

#-----------------------------------------------------------------------------

# method 3: By using lambda function
arr=[2,4,3,2,2,1,4,3,2,5,6,5,6,7,8]
rem_duplicate_fun=lambda arr:set(arr)
print(rem_duplicate_fun(arr))
