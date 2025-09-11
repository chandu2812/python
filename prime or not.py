num=int(input("enter the number :"))
lim=int(num/2)+1
for i in range(2,lim):
    rem=num%i
    if rem==0:
        print(num,"is not an prime number:")
        break
else:
    print(num,"is s a prime number:")
