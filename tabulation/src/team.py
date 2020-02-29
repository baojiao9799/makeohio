class Team:
    def __init__(self, name, scores, in_house):
        self.team_name = name
        self.tech = scores[0]
        self.cre = scores[1]
        self.imp = scores[2]
        self.pol = scores[3]
        self.wow = scores[4]
        self.in_house = in_house
        sum = 0
        for s in scores:
            sum += s
        self.sum = sum
        self.average = sum/5
