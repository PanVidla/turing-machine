from turing_machine import TuringMachine

initial_state = "init",
accepting_states = ["done"],
transition_function = {
    ("start", "0"): ("init", "0", "L"),
    ("start", "1"): ("init", "1", "L"),

    ("init", " "): ("right", "+", "R"),

    ("right", "0"): ("right", "0", "R"),
    ("right", "1"): ("right", "1", "R"),
    ("right", "*"): ("right", "*", "R"),
    ("right", " "): ("readB", " ", "L"),

    ("readB", "1"): ("addA", " ", "L"),
    ("readB", "0"): ("doubleL", " ", "L"),

    ("addA", "0"): ("addA", "0", "L"),
    ("addA", "1"): ("addA", "1", "L"),
    ("addA", "*"): ("read", "*", "L"),

    ("read", "+"): ("rewrite", "+", "L"),
    ("read", "1"): ("have1", "c", "L"),
    ("read", "0"): ("have0", "c", "L"),

    ("have0", "0"): ("have0", "0", "L"),
    ("have0", "1"): ("have0", "1", "L"),
    ("have0", "+"): ("add0", "+", "L"),

    ("add0", "O"): ("add0", "O", "L"),
    ("add0", "I"): ("add0", "I", "L"),
    ("add0", "0"): ("back0", "O", "R"),
    ("add0", " "): ("back0", "O", "R"),
    ("add0", "1"): ("back0", "I", "R"),

    ("back0", "0"): ("back0", "0", "R"),
    ("back0", "1"): ("back0", "1", "R"),
    ("back0", "O"): ("back0", "O", "R"),
    ("back0", "I"): ("back0", "I", "R"),
    ("back0", "+"): ("back0", "+", "R"),
    ("back0", "c"): ("read", "0", "L"),

    ("have1", "0"): ("have1", "0", "L"),
    ("have1", "1"): ("have1", "1", "L"),
    ("have1", "+"): ("add1", "+", "L"),

    ("add1", "O"): ("add1", "O", "L"),
    ("add1", "I"): ("add1", "I", "L"),
    ("add1", "0"): ("back1", "I", "R"),
    ("add1", " "): ("back1", "I", "R"),
    ("add1", "1"): ("carry", "O", "L"),

    ("carry", "1"): ("carry", "0", "L"),
    ("carry", "0"): ("back1", "1", "R"),
    ("carry", " "): ("back1", "1", "R"),

    ("back1", "0"): ("back1", "0", "R"),
    ("back1", "1"): ("back1", "1", "R"),
    ("back1", "O"): ("back1", "O", "R"),
    ("back1", "I"): ("back1", "I", "R"),
    ("back1", "+"): ("back1", "+", "R"),
    ("back1", "c"): ("read", "1", "L"),

    ("rewrite", "0"): ("rewrite", "0", "L"),
    ("rewrite", "1"): ("rewrite", "1", "L"),
    ("rewrite", "I"): ("rewrite", "1", "L"),
    ("rewrite", "O"): ("rewrite", "0", "L"),
    ("rewrite", " "): ("double", " ", "R"),

    ("double", "0"): ("double", "0", "R"),
    ("double", "1"): ("double", "1", "R"),
    ("double", "+"): ("double", "+", "R"),
    ("double", "*"): ("shift", "0", "R"),

    ("doubleL", "0"): ("doubleL", "0", "L"),
    ("doubleL", "1"): ("doubleL", "1", "L"),
    ("doubleL", "*"): ("shift", "0", "R"),

    ("shift", " "): ("tidy", " ", "L"),
    ("shift", "0"): ("shift0", "*", "R"),
    ("shift", "1"): ("shift1", "*", "R"),

    ("shift0", "0"): ("shift0", "0", "R"),
    ("shift0", "1"): ("shift1", "0", "R"),
    ("shift0", " "): ("read", "0", "R"),

    ("shift1", "1"): ("shift1", "1", "R"),
    ("shift1", " "): ("read", "1", "R"),
    ("shift1", "0"): ("shift0", "1", "R"),

    ("tidy", "0"): ("tidy", " ", "L"),
    ("tidy", "1"): ("tidy", " ", "L"),
    ("tidy", "+"): ("done", " ", "L"),
}
final_states = {"done"}

machine = TuringMachine("101*10",
                        initial_state="start",
                        final_states=final_states,
                        transition_function=transition_function)

print("Input:\n" + machine.get_tape())

step_counter = 0
while not machine.should_finish():

    machine.next_step()

    print("Step {}:\n{}".format(step_counter, machine.get_tape()))
    step_counter += 1

print("Result:\n")
print(machine.get_tape())
