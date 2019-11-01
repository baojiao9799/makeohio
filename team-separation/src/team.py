class Team:
    def __init__(self, data):
        self.team_name = data[0]
        self.member_names = data[1]
        self.member_emails = data[2]
        self.new = data[3]
        self.project_name = data[4]
        self.project_description = data[5]
        self.hardware = data[6]
        self.challenges = data[7]
        self.room = data[8]
        self.table = data[9]

        self.judge_pair_1 = None
        self.judge_pair_2 = None

    def room(elem):
        return elem.room

    def table(elem):
        return elem.table
