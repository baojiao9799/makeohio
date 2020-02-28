class Team:
    def __init__(self, name, scores):
        self.team_name = name
        self.tech = scores[0]
        self.pol = scores[1]
        self.imp = scores[2]
        self.cre = scores[3]
        self.wow = scores[4]
        sum = 0
        for s in scores:
            sum += s
        self.sum = sum
        self.average = sum/5
