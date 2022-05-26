#! /usr/bin/env python
"""Access point to the Deterministic Finite Automaton (DFA)
    The DFA works based on a definition that is in a given config file.
    ------------
    Functions
    ------------
    main:
        Access point to the DFA system. It controls the program's workflow.
"""


import input_output as io
import test
import DFA


def main():
    """Access point to the DFA system. It controls the program's workflow.
    """
    sigma = []
    states = []
    transitions = {}
    start_state = []
    final_state = []
    test_strings = []
    
    args = io.parse_input()
    config_file_path = args.input
    #output_file_path = args.output
    config_dict = io.load_config_file(config_file_path)
    #results = []

    # Input data validation
    sigma = config_dict["@sigma"].split(",")
    sigma = [sigma.strip("{ }") for sigma in sigma]

    states = config_dict["@Q"].split(",")
    states = [states.strip("{ }") for states in states]

    transitions = config_dict["@f"].split(",")
    transitions = [transitions.strip("{ }") for transitions in transitions]
    transitions = [transitions.strip("[ ]") for transitions in transitions]
    transitions_df = test.validate_transitions(transitions,states,sigma)

    start_state = config_dict["@q0"].split(",")
    start_state = test.validate_start_state(start_state, states)

    final_state = config_dict["@F"].split(",")
    final_state = [final_state.strip("{ }") for final_state in final_state]
    final_state = test.validate_final_states(final_state,states)

    test_strings = config_dict["@test"].split(",")
    test_strings = [test_strings.strip("{ }") for test_strings in test_strings]

    real_results = config_dict["@result"].split(",")
    real_results = [real_results.strip("{ }") for real_results in real_results]

    DFA.generate_automaton(sigma,
                            states,
                            transitions_df,
                            start_state,
                            final_state,
                            test_strings)

if __name__ == "__main__":
    main()