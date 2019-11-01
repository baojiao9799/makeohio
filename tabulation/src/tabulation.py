# tabulates results
# python 3 required - python3 tabulation.py
# Technical Difficulty,Intuitiveness,Impact/Usefulness,Creativity,Wow Factor
import csv, os
from team import Team

# get file from tabulation directory
DATA_DIRECTORY = '../data/'
filename = os.listdir(DATA_DIRECTORY)[0]
teams = {}

# open file and save teams
# collates all score into dict with scores
with open(DATA_DIRECTORY + filename) as data:
    reader = csv.reader(data)
    row_num = 0
    for row in reader:
        # teams start on row 3
        if row_num > 2:
            team_name = row[19]+row[20]+row[21]
            scores = row[24:29]
            if team_name in teams.keys():
                teams[team_name].append(scores)
            else:
                teams[team_name] = [scores]

        row_num+=1

final = []
# create average by criteria and complete average
# create team and add to new teams array
for team in teams:
    divisor = len(teams[team])
    sum = [0, 0, 0, 0, 0]
    for score in teams[team]:
        sum[0] += int(score[0])
        sum[1] += int(score[1])
        sum[2] += int(score[2])
        sum[3] += int(score[3])
        sum[4] += int(score[4])
    average = [x / divisor for x in sum]

    final.append(Team(team, average))

with open('../output/results.csv', mode='w') as results:
    results_writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['Team Name', 'Technical Difficulty', 'Intuitiveness', 'Impact/Usefulness', 'Creativity', 'Wow Factor', 'Total Average', 'Total Score'])
    for team in final:
        results_writer.writerow([team.team_name, team.tech, team.intu, team.imp, team.cre, team.wow, team.average, team.sum])


