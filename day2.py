from aocd import data

#convert to list of strings
cheatsheet = data.splitlines()

# Opponent: A=Rock, B=Paper, C=Scissor
# Self: X=Rock, Y=Paper, Z= Scissor
# Win = 6pts, Tie = 3pts, Loss = 1pt
# Rock = 1pt, Paper = 2pts, Scissors = 3pts


# if I wins : +6
# win scenarios: [A Y], [B Z], [C A]
# if tie: +3
# tie scenarios: [A X], [B Y], [C Z]
# if I lose: +1
# lose scenarios: [A Z], [B X], [C Y]


# Loop through cheatsheet
# cheatsheet[i][0] = opponent
# cheatsheet[i][2] = self

def find_score(guide):
    dict = {"X":1, "Y":2, "Z":3}
    total = 0
    for play in guide:
        opponent = play[0]
        self = play[2]
        total += dict.get(self)
        if (
            (opponent=="A" and self=="Y") or
            (opponent=="B" and self=="Z") or
            (opponent=="C" and self=="X")
            ):
            total += 6
        elif (
            (opponent=="A" and self=="X") or
            (opponent=="B" and self=="Y") or
            (opponent=="C" and self=="Z")
            ):
            total += 3
        else:
            pass
    return total


print(find_score(cheatsheet))