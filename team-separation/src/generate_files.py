# python 3 required - python3 generate_files.py
import csv, math, os
from printer import print_challenge_pdfs, print_general_pdfs, print_teams_in_room, merge_pdfs
from split_teams import split_teams
from team import Team
import companies as c
import rooms as r

JUDGES_COUNT = int(input('Number of judges: '))
JUDGE_PAIRS = int(JUDGES_COUNT/2)

# holds teams, and by challenge and room
teams = []
challenges = { c.AEP : [], c.HONDA : [], c.INNOVATION : []}
rooms = { r.MAKER1 : [], r.MAKER2 : [], r.MAKER3 : [], r.MAKER4 : [], r.MAKER5 : []}

# get file from team-registration directory
filename = os.listdir('../data')[0]

# open file and read through all teams
with open('../data/'+filename, errors = 'ignore') as data:
    reader = csv.reader(data)
    for row in reader:
        # row 6 True means complete survey
        if row[6] == 'True':
            # create a team object
            team = Team(row[17:32])
            teams.append(team)

            # add to room list
            rooms[team.room].append(team)

            # check if they chose challenge and add to challenge list
            for challenge in challenges:
                if challenge in team.challenges:
                    challenges[challenge].append(team)

##### CHALLENGE SHEETS #####
# Sort each challenge based on room and then room number
for challenge in challenges:
    challenges[challenge].sort(key=Team.room)
    challenges[challenge].sort(key=Team.table)
challenge_pdfs = print_challenge_pdfs(challenges)

##### GENERAL JUDGING SHEETS #####
judge_pairs = split_teams(teams, JUDGE_PAIRS)
general_pdfs = print_general_pdfs(judge_pairs)

##### PRINT COMBINED PDFS TO OUTPUT DIRECTORY #####
merge_pdfs('challenges.pdf', challenge_pdfs)
merge_pdfs('general.pdf', general_pdfs)

##### TEAM NAMES FOR JUDGING SURVEY #####
for room in rooms:
    # sort by table number
    rooms[room].sort(key=Team.table)
    print_teams_in_room(room, rooms[room])

# # Validate
# for team in teams:
#     if team.judge_pair_1 is None or team.judge_pair_2 is None or team.judge_pair_1 is team.judge_pair_2:
#         print('Failed, judging duplicate team :(')
#         print(team.team_name)


