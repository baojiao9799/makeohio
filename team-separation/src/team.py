class Team:
    def __init__(self, data):
        self.team_name = data[0]
        self.member_names = []
        j = 2
        for i in range(int(data[1]):
            self.member_names.append(data[j])
            j += 2
        self.member_emails = []
        j = 3
        for i in range(int(data[1]):
            self.member_emails.append(data[j])
            j += 2
        self.project_name = data[10]
        self.project_description = data[11]
        self.room = data[12]
        self.table = table[13]
        self.challenges = data[14]
        self.github = data[15]

        self.judge_pair_1 = None
        self.judge_pair_2 = None

    def room(elem):
        return elem.room

    def table(elem):
        return elem.table
