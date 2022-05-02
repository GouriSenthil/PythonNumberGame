#python program to concate two dictionaries
import random
number = random.randint(1,100)

print("        Rules for the game            ")
print("--------------------------------------")
print("Guess a number between 1 to 100")
print("You get 5 chances")

for i in range(0,5):
    print("Guess ",i+1,":")
    user = int(input("Enter the number"))
    if user == number:
        print("Hurray!!!")
        print("You guessed the number",number)
        break
    if user > number:
        print("Your guess is too high")
        continue
    if user < number:
        print("Your guess is too low")
        continue

if user != number:
   print("Your guess is incorrect the number is",number)

