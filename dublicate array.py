arr=list(map(int,input("enter the array elements").split()))
duplicate_array=[]
for num in arr:
    if num not in duplicate_array:
        duplicate_array.append(num)
print("duplicate array",duplicate_array)      

