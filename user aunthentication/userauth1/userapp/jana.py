a=int(input("enter the qauntity:"))
if a*100>1000:
    print("cost is:",((a*100)-(.1*a*100)))
else:
    print("cost is:",a*100)