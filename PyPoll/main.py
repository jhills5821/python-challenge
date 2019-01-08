import os
import csv

votes = []
canidatelist = []
canidatevotes = []
votepercent = []
winnertest = 0

bank_csv_path = os.path.join(".", "Input File", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

with open(bank_csv_path, newline="") as csvfile:
    csv_read = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_read)
    for row in csv_read:
        canidate=row[2]
        votes.append(canidate)
        x=len(votes)
        if canidate not in canidatelist:
            canidatelist.append(canidate)
            canidatevotes.append(0)
        for name in canidatelist:
            if name == canidate:
                y = canidatelist.index(canidate)
                canidatevotes[y] += 1
for vote in canidatevotes:
    if vote > winnertest:
        winnertest=vote
    a = canidatevotes.index(winnertest)
    winner = canidatelist[a]
    percent = (vote/x)
    votepercent.append(percent)

print("Election Results:")
print("-------------------")
print("Total Votes: ", x)

for each in canidatelist:
    z=canidatelist.index(each)
    print(str(canidatelist[z]),": ","{0:.3%}%".format(votepercent[z])," (",str(canidatevotes[z]),")")
print("-------------------")
print("Winner: ",winner)

with open("Output.txt", "w") as text_file:
    print("Election Results:", file=text_file)
    print("-------------------", file=text_file)
    print("Total Votes: ", x, file=text_file)

    for each in canidatelist:
        z=canidatelist.index(each)
        print(str(canidatelist[z]),": ","{0:.3%}%".format(votepercent[z])," (",str(canidatevotes[z]),")", file=text_file)
    print("-------------------", file=text_file)
    print("Winner: ",winner, file=text_file)