class LetterCountPolicy:
    min = 0
    max = 0
    letter = 'a'

    def __init__(self, mn, mx, letter):
        self.min = mn
        self.max = mx
        self.letter = letter

    def is_password_not_compliant(self, password):
        number_of_letters = len(list(filter(lambda x: x == self.letter, list(password))))
        return number_of_letters < self.min or number_of_letters > self.max


class LetterPositionPolicy:
    position_one = 0
    position_two = 0
    letter = 'a'

    def __init__(self, p_one, p_two, letter):
        self.position_one = p_one
        self.position_two = p_two
        self.letter = letter

    def is_password_not_compliant(self, password):
        letters = list(password)
        return not (letters[self.position_one - 1] == self.letter and letters[self.position_two - 1] != self.letter or \
               letters[self.position_one - 1] != self.letter and letters[self.position_two - 1] == self.letter)
