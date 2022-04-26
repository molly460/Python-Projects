guessing_word = "python"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != guessing_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of Guesses, YOU LOSE!")
else:
    print("You Win")
