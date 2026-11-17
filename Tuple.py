#Calculate the average of 5 numbers stored in a tuple.
numbers = ()

for i in range(5):
    num = int(input("Enter a number: "))
    numbers = numbers + (num,)

total = 0

for num in numbers:
    total = total + num

average = total / 5

print("Entered numbers:", numbers)
print("Sum:", total)
print("Average:", average)
