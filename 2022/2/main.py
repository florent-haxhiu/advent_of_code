# Outcome of round
# Win  = 6
# Draw = 3
# Loss = 0

with open("test-data.txt") as f:
    a = [item for item in f.read().splitlines()]

b = []
score = 0
elf = 0

for line in a:
    b.append(line.split())

# A, X = Rock     => Points = 1
# B, Y = Paper    => Points = 2
# C, Z = Scissors => Points = 3

# X is now Lose
# Y is now Draw
# Z is now Win


def get_points_each_round():
    for game in b:
        win(game)


def win(game):
    global score
    comp = game[0]
    me = game[1]
    if comp == "A" and me == "X":
        score += 3  # For the choice
        score += 0  # For the draw
    elif comp == "A" and me == "Y":
        score += 1
        score += 3
    elif comp == "A" and me == "Z":
        score += 2
        score += 6
    elif comp == "B" and me == "X":
        score += 1
        score += 0
    elif comp == "B" and me == "Y":
        score += 2
        score += 3
    elif comp == "B" and me == "Z":
        score += 3
        score += 6
    elif comp == "C" and me == "X":
        score += 2
        score += 0
    elif comp == "C" and me == "Y":
        score += 3
        score += 3
    elif comp == "C" and me == "Z":
        score += 1
        score += 6


get_points_each_round()
print(score)
