#assignment 1
word = input("Enter a word: ")
word = word.lower()

first_array = []
second_array = []

for index in range(0,len(word)):
    first_array.append(word[index])

for index in range(len(word)-1,-1,-1):
    second_array.append(word[index])

if first_array == second_array:
    print("palindrome")
else:
    print("not palindrome")


#assignment 2

word = input("Enter a word: ")
word = word.lower()

first_array = []
second_array = []

for index in range(0,len(word)):
    first_array.append(word[index])

for index in range(len(word)-1,-1,-1):
    second_array.append(word[index])

if first_array == second_array:
    print("palindrome")
else:
    print("not palindrome")

    #assignment 3

    numbers = int(input("Enter a number: "))

x = number-1
prime = True

while x > 1:
    if number % x == 0:
        prime = False
    x = x-1

if prime == True:
    print("Prime")
else:
    print("Not Prime")
