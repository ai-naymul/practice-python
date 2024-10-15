from generate_random_number import GenerateNumber


user_input_start = int(input("Give the strating range of the number "))
user_input_end = int(input("Give the ending range of the number "))


generate_number = GenerateNumber()
generated_number = generate_number.generate_random_number(start = user_input_start, end = user_input_end)


for i in range(user_input_end):
    guess = int(input("Guess the number "))
    if guess == generated_number:
        print("Woooohhoooo, Congrats you guessed the number")
        break
    elif guess > generated_number:
        print("Too high try a lower value")
    elif guess < generated_number:
        print("Too low try a higher value")
    else:
        print("Give a invalid input")
