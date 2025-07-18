correct_pin='1234'
attempt=0
while attempt <2:
    print("attempt:",attempt+1)
    pin=input("enter your PIN:")
    if pin==correct_pin:
       print("access granted")
       break
    else:
     print("wrong PIN.")
    attempt +=1
else:
 print("too many attempts! Access blocked")
