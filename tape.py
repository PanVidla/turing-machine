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

            min_used_index = min(self.tape.keys())
            max_used_index = max(self.tape.keys())
            if index < min_used_index:

                new_min_index = min_used_index - 1
                new_position = {new_min_index: self.blank}
                self.tape = new_position | self.tape

                print("Enlarging tape:")
                print(self.tape)

            if index > max_used_index:

                new_max_index = max_used_index + 1
                new_position = {new_max_index: self.blank}
                self.tape = self.tape | new_position

                print("Enlarging tape:")
                print(self.tape)

    def __setitem__(self, pos, char):
        self.tape[pos] = char
