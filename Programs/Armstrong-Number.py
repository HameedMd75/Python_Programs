
num = int(input("Enter a number: "))
order = len(str(num))
sum_digits = sum(int(digit) ** order for digit in str(num))
print("Armstrong" if num == sum_digits else "Not Armstrong")