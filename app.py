# Description: A simple Rock, Paper, Scissors game that allows the user to play against the computer.
import random


def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose rock, paper, or scissors to play against the computer.")
    print("Type 'quit' to end the game.")
    print("")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "quit":
            print("Final score: You: " + str(user_score) + " Computer: " + str(computer_score))
            break

        if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer chose: " + computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print("Score: You: " + str(user_score) + " Computer: " + str(computer_score))
        print("")

        # Ask the user to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "no" or play_again == "n" or play_again == "quit":
            print("Final score: You: " + str(user_score) + " Computer: " + str(computer_score))
            break


if __name__ == "__main__":
    main()
