scores_dictionary = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
# Ganar 6, Empatar 3
# Usar la X 1, Usar la Y 2, Usar la Z 3

scores_part2 = {"A Z": 6+2, "A Y": 3+1, "A X": 3, "B Z": 6+3, "B Y": 3+2, "B X": 1, "C Z": 6+1, "C Y": 3+3, "C X": 2}
# Ganar 6, Empatar 3
# X ganar, Y Empatar, Z perder
# Rock 1, Paper 2, Scissors 3

with open("input_day02.txt") as f:
    lines = f.readlines()
total = 0

for i in lines:
    total += scores_part2[i.strip()]
print(total)
