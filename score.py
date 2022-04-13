
class Score(object):
    def __init__(self):
        self._score = 0
    def change_score(self,number):
        self._score +=number
    def get_score(self):
        return self._score
    def write_score_to_table(self):
        with open('score1.txt', 'w') as file:
            file.write(str(self._score))
    def load_score_to_screen(self):
        with open('score1.txt', 'r') as file:
               return file.readlines()
