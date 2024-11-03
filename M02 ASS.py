# 4.1 Choose a number between 1 and 10 and assign it to the variable secret. Then, select another number between 1 and 10 and assign it to the variable guess. Next, write the conditional tests (if, else, and elif) to print the string 'too low' if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret.

def guessMyNumber():[1,2,3,4,5,6,7,8,9,10]
secretNumber = 6
guess = 0
while guess != secretNumber:
    guess = int(input("Guess a number between 1 and 10: "))
if guess < secretNumber:
    print("too low! Try again.")
elif guess > secretNumber:
    print("too high! Try again.")
else:
    print("just right")

# 4.2 Assign True or False to the variables small and green. Write some if/else statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.

small = True
green = False
if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")


# 6.1 Use a for loop to print the values of the list [3, 2, 1, 0].
list = [3,2,1,0]
sum = 0
for list in list:
    sum += list
    print(sum)
    

# 6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number. Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess me. If number equals guess_me, print 'found it!' and then exit the loop. If number is greater than guess_me, print 'oops' and then exit the loop. Increment number at the end of the loop.

    guess_me = 7
    number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1

# 6.3 Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable called number over range(10). If number is less than guess_me, print 'too low'. If it equals guess_me, print found it! and then break out of the for loop. If number is greater than guess_me, print 'oops' and then exit the loop.

guess_me = 5
for number in range (10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it ! ")
        break
    else:
        print("oop")
        break


