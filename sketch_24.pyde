"Assignment 24, Sorting - Julie Anne Camina, 87244@gscs.ca"

#opens randnum text file and reads all the numbers written on it, empty list used to store every line on txt file
data = open("randnum.txt", 'r')
numbers = []

#puts all the numbers on the file into the empty list and removes the /n
for line in data:
    numbers.append(line.rstrip())    

#goes through all the numbers, swapped being false because we haven't changed anything to the list yet
for i in range(len(numbers)):
    swapped = False
    #loop to compare the numbers
    for j in range(0, len(numbers)-i-1):
        #compares 2 adjacent numbers, starting with numbers[0] and numbers[1], swapped being true because we have now changed things
        if numbers[i] > numbers[i+1]:
            #swaps if the first number is bigger than the other
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            swapped = True
            print(i, i+1)
        if swapped is not False:
            break

            
print(numbers, i, i+1)
