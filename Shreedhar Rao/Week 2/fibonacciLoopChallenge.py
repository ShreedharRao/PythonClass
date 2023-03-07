# write code for the fibonacci sequence
print("this is the first 10 fibonacci sequence numbers")
x1 = 0
x2 = 1
next = 0
counter = 1
while counter <= 10:
    next = x1 + x2
    x1 =x2
    x2 = next
    print(next)
    counter = counter + 1