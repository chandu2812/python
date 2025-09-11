a=eval(input("enter the marks out of 300 :"))
b=a/300*100
print("percentage is ",b)
if(a>300):
    print("invalid marks ")
elif(b>90):
    print("A grade")
elif(b>80):
    print("B grade")
elif(b>50):
    print("C grade")
elif(b>40 and b<50):
    print("D grade")
else:
    print("fail")