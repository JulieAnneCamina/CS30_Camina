data = open("randnum.txt", 'r')
numbers = []

for line in data:
    numbers.append(line.rstrip())
    
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[i]:
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp
            
print(numbers)
        
