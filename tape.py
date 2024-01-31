class Tape(object):

    blank = " "

    def __init__(self, tape_string=""):
        self.tape = dict((enumerate(tape_string)))

    def __str__(self):
        s = ""
        min_used_index = min(self.tape.keys())
        max_used_index = max(self.tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.tape[i]
        return s

    def __getitem__(self, index):
        if index in self.tape:
            return self.tape[index]
        else:
            return Tape.blank

    def __setitem__(self, pos, char):
        self.tape[pos] = char
