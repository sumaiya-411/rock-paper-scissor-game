import random

def get_user_choice():
    print("\nPick one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    choices = {
        "1": "rock",
        "2": "paper",
        "3": "scissors"
    }
    
    return choices.get(choice)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "lose"

# Main game loop
def main():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins the match!")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()

        if not user_choice:
            print("Oops! That's not a valid choice. Try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\n🧑 You picked: {user_choice}")
        print(f"🤖 Computer picked: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "win":
            print("✅ You win this round!")
            user_score += 1
        elif result == "lose":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("😐 It's a draw!")

        print(f"📊 Score: You {user_score} - {computer_score} Computer")

        if user_score == 5:
            print("\n🎉 Congrats! You won the match!")
            break
        elif computer_score == 5:
            print("\n💻 Computer wins the match. Better luck next time!")
            break

        play_again = input("\nPlay another round? (y/n): ").strip().lower()
        if play_again != "y":
            print("\n👋 Thanks for playing! See you next time!")
            break

# Run the game
if __name__ == "__main__":
    main()
