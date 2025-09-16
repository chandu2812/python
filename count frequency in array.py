def count_frequency(arr):
    frequency={}
    for element in arr:
        if element in frequency:
            frequency[element]+=1
        else:
            frequency[element]=1
    return frequency
arr=[1,2,1,1,5,8,9,9,6,8,8,9,4]
result=count_frequency(arr)
print("array:",arr)
print("elements frequency:")
for elements,count_frequency in result.items():
    print(f"{elements}:{count_frequency} times(s)")        

    
