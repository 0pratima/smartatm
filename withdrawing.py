pin="12345"
balance=10000

p=input("enter your pin:")
if p==pin:
 print("access granted")
 choice=input("Enter'withdraw'or 'check':").lower()
 if choice=="withdraw":
    amount=int(input("Enter the amount to withdraw:"))
    if amount<=balance:
      balance-=amount
      print(f"withdraw {amount}.Remaining balance:{balance}")
    else:
      print("Insufficient funds.")
 elif choice=="check":
    print(f"your current balance is {balance}")
else:
  print("Invalid option.")
