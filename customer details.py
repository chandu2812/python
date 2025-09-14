
name = input("Enter Customer Name: ")
mobile = input("Enter Mobile Number: ")
cost = float(input("Enter Cost of Purchase: "))

if cost > 5000:
    discount = cost * 0.10   
elif cost > 2000:
    discount = cost * 0.05   
else:
    discount = 0

total = cost - discount

print("\n--- Bill Details ---")
print("Customer Name  :", name)
print("Mobile Number  :", mobile)
print("Purchase Cost  :", cost)
print("Discount       :", discount)
print("Total Amount   :", total)
