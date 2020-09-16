while True:
    x = int(input("Enter a integer: "))
    if x == 0:
        break
    elif x < 0:
        continue
    print("Square is {} ".format(x * x))