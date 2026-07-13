num = int(input("Enter a number:"))
sum = 0
temp = num
while temp > 0:
    remain = temp % 10
    cubed = remain ** 3
    sum = sum + cubed
    temp = temp // 10 
    
if num == sum:
    print ( num, "is an armstrong number.")
else: print (num, "is not an armstrong number ")