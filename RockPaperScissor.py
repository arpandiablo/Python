import random
options = ["Rock","Paper","Scissor"]
results = [ ["Draw","You Lost","You Won"],["You Won","Draw","You Lost" ],["You Lost","You Won","Draw"]]
while True:
    userinp = input("Choose between Rock Paper and Scissor and \"Exit\" to Quit: ")
    compinp = random.choice(options)
    if userinp==compinp:
        print(f"Oops! Computer chose {compinp} too. The Game is Drawn")
    elif userinp=="Exit":
        print("Thanks for Playing")
        break
    elif userinp in options:
        print(f"The Computer chose {compinp}.")
        flag = results[options.index(userinp)][options.index(compinp)]
        print(f"{flag}")
    else:
        print("Invalid Option")

#     R P S
# R   D L W
# P   W D L
# S   L W D