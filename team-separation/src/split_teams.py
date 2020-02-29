import math, random

def split_teams(teams, JUDGE_PAIRS):
    judge_pairs = {}
    for i in range(JUDGE_PAIRS):
        judge_pairs[i+1] = []

    MAX_TEAMS = math.ceil(len(teams)*2/JUDGE_PAIRS)

    # first round of teams
    temp_teams = teams.copy()
    random.shuffle(temp_teams)
    pair_num=1
    for team in temp_teams:
        team.judge_pair_1 = pair_num
        judge_pairs[pair_num].append(team)
        pair_num = (pair_num+1)%(JUDGE_PAIRS+1)

    # second round of teams
    temp_teams = teams.copy()
    random.shuffle(temp_teams)
    pair_num=1
    for team in temp_teams:
        while team.judge_pair_1 is pair_num or len(judge_pairs[pair_num]) > MAX_TEAMS:
            pair_num = (pair_num+1)%(JUDGE_PAIRS+1)
        team.judge_pair_2 = pair_num
        judge_pairs[pair_num].append(team)
        pair_num = (pair_num+1)%(JUDGE_PAIRS+1)
    return judge_pairs
