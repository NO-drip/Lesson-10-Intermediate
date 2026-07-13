calculate_base = int(input("Enter a number."))
calculate_expo = int(input("Enter the power number to raise."))
result = 1
for x in range(calculate_expo):
    result = result * calculate_base
    print (result)
