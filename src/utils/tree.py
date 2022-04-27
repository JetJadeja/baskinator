class DecisionTree:
    def __init__(self, data):
        self.yes = None
        self.no = None
        self.data = data

    def insert_yes(self, data):
        self.yes = DecisionTree(data)
        return self.yes

    def insert_no(self, data):
        self.no = DecisionTree(data)
        return self.no