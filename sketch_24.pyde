data = open("randnum.txt", 'r')
numbers = []

for line in data:
    numbers.append(line.rstrip())    

for i in range(len(numbers)):
    swapped = False
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True
        if swapped == False:
            break
            

print(numbers)
