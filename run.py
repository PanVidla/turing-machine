from turing_machine import TuringMachine

initial_state = "init",
accepting_states = ["finish"],
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

    ("read", "+"): ("rewrite", "+", "L"),
    ("read", "1"): ("have1", "c", "L"),
    ("read", "0"): ("have0", "c", "L"),

    ("have0", "0"): ("have0", "0", "L"),
    ("have0", "1"): ("have0", "1", "L"),
    ("have0", "+"): ("add0", "+", "L"),

    ("add0", "O"): ("add0", "O", "L"),
    ("add0", "I"): ("add0", "I", "L"),
    ("add0", "0"): ("back0", "O", "R"),
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
    ("add1", "0"): ("back1", " ", "R"),
    ("add1", " "): ("back1", " ", "R"),
    ("add1", "1"): ("carry", "O", "L"),

    ("carry", "1"): ("carry", "0", "L"),
    ("carry", "0"): ("back1", "0", "L"),
}
final_states = {"finish"}

machine = TuringMachine("101*10",
                        initial_state="start",
                        final_states=final_states,
                        transition_function=transition_function)

print("Input:\n" + machine.get_tape())

while not machine.should_finish():
    machine.next_step()

print("Result:")
print(machine.get_tape())
