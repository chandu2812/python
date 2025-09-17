import math
def is_perfect(n):
    if n<0:
        return False
    root=math.isqrt(n)
    return root*root==n
num=(int(input("enter number: ")))
if is_perfect(num):
    print(f"{num}is perfect square")
else:
    print(f"{num}is NOT a perfect number ")
    