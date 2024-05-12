import random
options = ["Rock","Paper","Scissor"]
results = [ ["Draw","You Lost","You Won"],["You Won","Draw","You Lost" ],["You Lost","You Won","Draw"]]
userinp = input("Choose between Rock Paper and Scissor and \"Exit\" to Quit: ")
compinp = random.choice(options)
while True:
    if userinp==compinp:
        print(f"Oops! Computer chose {compinp} too. The Game is Drawn")
    elif userinp=="Exit":
        print("Thanks for Playing")
        break
    else:
        flag = results[userinp][compinp]
        print(f"{flag}")

#     R P S
# R   D L W
# P   W D L
# S   L W D