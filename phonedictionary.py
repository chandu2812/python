n=int(input("enter the limit"))
m={}
mob=0
name=" "
i=0
for i in range(0,n):
    mob=int(input("enter the mobile number :"))
    name=str(input("enter name "))
    z2=dict({mob:name})
    m.update(z2)
print(m)
n=int(input("enter the no to search in dictionary"))
print("the name of the person is ",m[n])
