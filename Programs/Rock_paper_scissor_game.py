import random
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors:) ")
  options =["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice , "computer" : computer_choice}
  return choices

def check_win(player, computer):
  print(f"you choose {player}, computer choose {computer}")
  if player == computer:
    return "its a tie"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! you win!"
    else:
      return "papers covers rocks! you lose."
  elif player == "paper":
    if computer == "rock":
      return "paper covers rocks! you win!"
    else:
      return "scissor cuts paper! you lose."
  elif player == "scissors":
    if computer == "paper":
      return "scissor cuts paper! you win!."
    else:
      return "Rock smashes scissors! you lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
