# When divisible by 3 it should display "Fizz".
# When divisible by 5 it should display "Buzz".
# When divisible by 3 or 5 it should display "Fizz Buzz".

# [Basic Game]
# - By Using PF concepts:
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# - By Using OOP concepts:
class FizzBuzzGame():
    def play(self):
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
object = FizzBuzzGame()
object.play()

# [Game According To Project Requirement]
import random 
print("Here I,am Presenting you the Fizz-Buzz Game.")
print("Rules of the game are:")
print("1 - When divisible by 3 it should display Fizz.")
print("2 - When divisible by 3 it should display Buzz.")
print("3 - Or else just display the Number.")
x = random.randint(1, 100)
while True:
    if x % 3 == 0 and x % 5 == 0:
        answer = "FizzBuzz"
    elif x % 3 == 0:
        answer = "Fizz"
    elif x % 5 == 0:
        answer = "Buzz"
    else:
        answer = str(x)

    y = input(f"Number: {x}, My Answer:")
    if y != answer:
        print(f"Your Game Is Over! The right answer is {answer}")
        break
    else:
        print("Your Answer Is Perfectly Right!")

    new_num = random.randint(1, 100)
    x = x + new_num



# [To Handle Spaces Or Small Letters We Can Use .strip(.lower())]
import random 
print("Here I,am Presenting you the Fizz-Buzz Game.")
print("Rules of the game are:")
print("1 - When divisible by 3 it should display Fizz.")
print("2 - When divisible by 3 it should display Buzz.")
print("3 - Or else just display the Number.")
x = random.randint(1, 100)
while True:
    if x % 3 == 0 and x % 5 == 0:
        answer = "FizzBuzz"
    elif x % 3 == 0:
        answer = "Fizz"
    elif x % 5 == 0:
        answer = "Buzz"
    else:
        answer = str(x)

    y = input(f"Number: {x}, My Answer:").strip().lower()
    if answer in ("Fizz", "Buzz", "FizzBuzz"):
        ans = answer.lower()
    else: 
        ans = answer

    if y != ans:
        print(f"Your Game Is Over! The right answer is {answer}")
        break 
    else:
        print("Your Answer Is Perfectly Right!")

    new_num = random.randint(1, 100)
    x = x + new_num