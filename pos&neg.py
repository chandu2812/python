
pos=[]
neg=[]
while True:
    n= int(input())
    if n == -1:
        break
    (pos if n>0 else neg).append(n) if n!=0 else None
print("avg negative number is ",sum(neg)//len(neg),
        ",avg positive number is",sum(pos)//len(pos))
    
    


