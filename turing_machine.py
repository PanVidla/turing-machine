from tape import Tape


class TuringMachine(object):

    def __init__(self,
                 tape="",
                 blank_symbol=" ",
                 initial_state="",
                 final_states=None,
                 transition_functions=None):
        self.tape = Tape(tape)
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state

        if transition_functions is None:
            self.transition_function = {}
        else:
            self.transition_function = transition_functions

        if final_states is None:
            self.final_states = set()
        else:
            self.final_states = set(final_states)

    def get_head(self):

        head_position_string = ""

        for position in self.tape.tape.keys():
            if position == self.head_position:
                head_position_string += "^"
            else:
                head_position_string += " "

        return head_position_string

    def get_tape(self):
        return str(self.tape)

    def next_step(self):

        current_character = self.tape[self.head_position]
        x = (self.current_state, current_character)

        if x in self.transition_function:

            y = self.transition_function[x]
            self.tape[self.head_position] = y[1]

            if y[2] == "R":
                self.head_position += 1

            elif y[2] == "L":
                self.head_position -= 1

            self.current_state = y[0]

    def should_finish(self):
        if self.current_state in self.final_states:
            return True
        else:
            return False
