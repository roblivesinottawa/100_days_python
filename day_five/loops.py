scores = input("enter a list of all student's scores: >>> ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

highest_score = scores[0]
for score in scores:
    if score > highest_score:
        highest_score = score
print(f"the highest score in class is {highest_score}")


# highest_score = max(scores)
# print(highest_score)
