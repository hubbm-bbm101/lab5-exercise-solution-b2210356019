N = int(input("Please enter a number: "))
even_sum = 0
odd_sum = 0
count = 0

for number in range(1, N + 1):
    if number % 2 == 0:
        count = count + 1
        even_sum = even_sum + number
    else:
        odd_sum = odd_sum + number

even_average = even_sum / count
print("Average of even numbers: " + str(even_average))
print("Sum of odd numbers: " + str(odd_sum))
