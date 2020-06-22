from random import randint, randrange
import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter Number of Players>"))
while num > 4 or num < 2:
    print("Minimum number of players must be 2 And Maximum must be 4")
    num = int(input("Enter Number of Players>"))

scores = [0, 0, 0, 0]
i = 1
turns = 0
# temp_score = [0, 0, 0, 0]
turn_score = [[0, 0, 0, 0]]

max_score = max(scores)

while max_score < 23:
    while i <= num:
        f_num = randint(1, 6)
        s_num = randint(1, 6)
        if f_num == 1 or s_num == 1:
            scores[i - 1] += 0
            # temp_score[i - 1] += 0
            i += 1
        elif f_num == 1 and s_num == 1:
            scores[i - 1] = 0
            # temp_score[i - 1] = 0
            i += 1
        else:
            scores[i - 1] += f_num + s_num
            # temp_score[i - 1] += f_num + s_num
            i += 1
    i = 1
    turns += 1
    turn_score.append(scores[:])
    max_score = max(scores)

print(turn_score)
print(scores)
print(f"Player {scores.index(max_score) + 1} Wins by {max_score} points after {turns} turns")

turns += 1

x = np.arange(0, turns)
n = 0
p1 = []
p2 = []
p3 = []
p4 = []
while n < turns:
    p1.insert(n, turn_score[n][0])
    p2.insert(n, turn_score[n][1])
    p3.insert(n, turn_score[n][2])
    p4.insert(n, turn_score[n][3])
    n += 1

plt.plot(x, p1, label="Player 1")
plt.plot(x, p2, label="Player 2")
plt.plot(x, p3, label="Player 3")
plt.plot(x, p4, label="Player 4")

plt.xlabel("Turns")
plt.ylabel("Points")

plt.title("Pig Game Scores")
plt.legend()
plt.show()


